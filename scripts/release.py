#!/usr/bin/env python3
"""Validate a checked-out release tag and optionally upload a draft release."""
import argparse
import hashlib
import json
import os
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from validate import ROOT, read_json, validate
from package import git_identity, package_files, archive_bytes


def check(tag, root=ROOT):
    if not re.fullmatch(r'v\d+\.\d+\.\d+', tag):
        raise ValueError('Release tag must have the form v0.1.0')
    commit = subprocess.check_output(['git', '-C', str(root), 'rev-parse', '--verify', f'refs/tags/{tag}^{{commit}}'], text=True).strip()
    identity = git_identity(root)
    if identity != {'commit': commit, 'dirty': False}:
        raise ValueError('Build the selected tag commit from a clean checkout')
    if read_json(root / 'package.json')['version'] != tag[1:]:
        raise ValueError('Tag and package versions differ')
    if read_json(root / 'sources/lock.json')['release'] != tag[1:]:
        raise ValueError('Tag and source lock release versions differ')
    report = validate(root)
    if not report['ok']:
        raise ValueError('; '.join(report['errors'][:10]))
    return commit


def request(url, token, *, data=None, content_type='application/json'):
    headers = {'Authorization': f'Bearer {token}', 'Accept':'application/vnd.github+json',
               'X-GitHub-Api-Version':'2026-03-10', 'User-Agent':'workshop-overpy-skills-release'}
    if data is not None:
        headers['Content-Type'] = content_type
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=60) as response:
        return json.load(response)


def verify_artifacts(tag, commit, root=ROOT):
    files = [root/'dist'/f'{kind}-skills-{tag[1:]}.zip' for kind in ('workshop','workshop-overpy')]
    checksums = (root/'dist/SHA256SUMS').read_text()
    for file, skills in zip(files, [('overwatch-workshop',), ('overwatch-workshop','overpy')]):
        if f'{hashlib.sha256(file.read_bytes()).hexdigest()}  {file.name}\n' not in checksums:
            raise ValueError(f'Checksum mismatch for {file.name}')
        expected = archive_bytes(package_files(root, skills, {'commit':commit,'dirty':False}, tag[1:], read_json(root/'sources/lock.json')))
        if file.read_bytes() != expected:
            raise ValueError(f'{file.name} differs from the files and metadata in the selected checkout')
        with zipfile.ZipFile(file) as archive:
            manifest = json.loads(archive.read('RELEASE.json'))
            if manifest['repository'] != {'commit':commit,'dirty':False} or manifest['version'] != tag[1:]:
                raise ValueError(f'{file.name} was not built from the selected clean tag')
            if manifest['source_locks'] != read_json(root/'sources/lock.json'):
                raise ValueError(f'{file.name} has stale source locks')
            if set(archive.namelist()) != set(manifest['files']) | {'RELEASE.json'}:
                raise ValueError(f'{file.name} has unexpected contents')
            for name, digest in manifest['files'].items():
                if hashlib.sha256(archive.read(name)).hexdigest() != digest:
                    raise ValueError(f'{file.name}: member hash mismatch')
    return files


def draft(tag, root=ROOT):
    commit = check(tag, root)
    files = verify_artifacts(tag, commit, root)
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    token = os.environ.get('GITHUB_TOKEN', '')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) or not token:
        raise ValueError('GITHUB_REPOSITORY and GITHUB_TOKEN are required to create a draft')
    base = os.environ.get('GITHUB_API_URL', 'https://api.github.com').rstrip('/')
    if not base.startswith('https://'):
        raise ValueError('GitHub API must use HTTPS')
    try:
        request(f'{base}/repos/{repository}/releases/tags/{tag}', token)
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise
    else:
        raise ValueError('A release already exists for this tag; refusing to replace its assets')
    body = {'tag_name':tag,'target_commitish':commit,'name':f'Workshop and OverPy skills {tag}',
            'draft':True,'prerelease':True,
            'body':'Portable Markdown skills. Workshop works independently; OverPy requires the included matched Workshop version. Compiler checks are separate from in-game verification. See INSTALL.md, THIRD_PARTY_NOTICES.md, RELEASE.json, and SHA256SUMS in the downloads.'}
    release = request(f'{base}/repos/{repository}/releases',token,data=json.dumps(body).encode())
    for file in files + [root/'dist/SHA256SUMS', root/'dist/context-report.json']:
        url=release['upload_url'].split('{')[0]+'?name='+urllib.parse.quote(file.name)
        request(url,token,data=file.read_bytes(),content_type='application/zip' if file.suffix=='.zip' else 'application/octet-stream')
    return {'draft_url':release['html_url'],'commit':commit,'published':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=('check','draft'))
    parser.add_argument('--tag',default=os.environ.get('RELEASE_TAG',''))
    args=parser.parse_args()
    try:
        result=draft(args.tag) if args.command=='draft' else {'commit':check(args.tag),'tag':args.tag}
        print(json.dumps(result,indent=2))
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1,f'{exc}\n')


if __name__=='__main__':
    main()
