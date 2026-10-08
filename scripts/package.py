#!/usr/bin/env python3
"""Build deterministic standalone Workshop and matched-pair skill archives."""
import argparse
import hashlib
import io
import json
import subprocess
import sys
import zipfile
from pathlib import Path

from validate import ROOT, SKILLS, read_json, validate


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + '\n').encode()


def archive_bytes(files):
    """Fixed metadata and stored entries avoid platform/zlib-dependent output."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, content in sorted(files.items()):
            if Path(name).is_absolute() or '..' in Path(name).parts or '\\' in name:
                raise ValueError(f'Unsafe package path: {name}')
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, content)
    return buffer.getvalue()


def git_identity(root):
    def git(*args):
        return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()
    try:
        return {'commit': git('rev-parse', 'HEAD'), 'dirty': bool(git('status', '--porcelain', '--untracked-files=normal'))}
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {'commit': None, 'dirty': None}


def collect_files(root, skills):
    files = {}
    for name in skills:
        for file in sorted((root / 'skills' / name).rglob('*')):
            if file.is_symlink():
                raise ValueError(f'Skill symlink cannot be packaged: {file}')
            if not file.is_file():
                continue
            if file.suffix not in ('.md', '.opy', '.workshop', '.json'):
                raise ValueError(f'Unexpected skill file: {file}')
            # All installable files are text; line endings are normalized.
            files[file.relative_to(root / 'skills').as_posix()] = file.read_text(encoding='utf-8').replace('\r\n', '\n').encode()
    for name in ('LICENSE', 'THIRD_PARTY_NOTICES.md', 'INSTALL.md'):
        files[name] = (root / name).read_text().replace('\r\n', '\n').encode()
    return files


def package_files(root, skills, identity, version, source_lock):
    files = collect_files(root, skills)
    manifest = {'schema_version':1, 'version':version, 'skills':list(skills), 'repository':identity,
                'source_locks':source_lock, 'generator_version':1,
                'dependency':{'overpy_requires_workshop':version} if 'overpy' in skills else {},
                'files':{k:hashlib.sha256(v).hexdigest() for k,v in sorted(files.items())},
                'manifest_note':'File hashes exclude RELEASE.json itself; package SHA-256 is external.'}
    files['RELEASE.json'] = json_bytes(manifest)
    return files


def verify_freshness(root):
    for command in (['node', str(root/'scripts/generate-api.mjs'), '--check'],
                    [sys.executable, str(root/'scripts/generate-wiki.py'), '--check']):
        result = subprocess.run(command, cwd=root, capture_output=True, text=True)
        if result.returncode:
            raise ValueError('Generated content is stale: ' + (result.stdout + result.stderr).strip())


def verify_archives(root, version, identity, destination=None):
    """Bind on-disk packages to actual checkout contents, not their own manifests."""
    destination = Path(destination or root / 'dist')
    checksums = (destination / 'SHA256SUMS').read_text()
    files = []
    for kind, skills in [('workshop', SKILLS[:1]), ('workshop-overpy', SKILLS)]:
        file = destination / f'{kind}-skills-{version}.zip'
        content = file.read_bytes()
        if f'{hashlib.sha256(content).hexdigest()}  {file.name}\n' not in checksums:
            raise ValueError(f'Checksum mismatch for {file.name}')
        expected = archive_bytes(package_files(root, skills, identity, version, read_json(root / 'sources/lock.json')))
        if content != expected:
            raise ValueError(f'{file.name} differs from the files and metadata in the selected checkout')
        files.append(file)
    return files


def build(root=ROOT, destination=None, release=False):
    root = Path(root).resolve()
    destination = Path(destination or root / 'dist').resolve()
    verify_freshness(root)
    report = validate(root)
    if not report['ok']:
        raise ValueError('Validation failed: ' + '; '.join(report['errors'][:20]))
    source_lock = read_json(root / 'sources/lock.json')
    version = read_json(root / 'package.json')['version']
    identity = git_identity(root)
    if release and (identity['dirty'] is not False or not identity['commit']):
        raise ValueError('Release packages require a clean Git checkout')
    destination.mkdir(parents=True, exist_ok=True)
    checksums, shared = {}, None
    for suffix, skills in [('workshop', SKILLS[:1]), ('workshop-overpy', SKILLS)]:
        files = package_files(root, skills, identity, version, source_lock)
        workshop = {k:v for k,v in files.items() if k.startswith('overwatch-workshop/')}
        if shared is not None and shared != workshop:
            raise ValueError('Workshop content differs between packages')
        shared = workshop
        first = archive_bytes(files)
        second = archive_bytes(dict(reversed(list(files.items()))))
        if first != second:
            raise ValueError('Non-reproducible package')
        filename = f'{suffix}-skills-{version}.zip'
        (destination / filename).write_bytes(first)
        checksums[filename] = hashlib.sha256(first).hexdigest()
        # Reopen actual archives; compare each member with the inputs used in the manifest.
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            if set(archive.namelist()) != set(files):
                raise ValueError('Package content mismatch')
            for name, content in files.items():
                if archive.read(name) != content:
                    raise ValueError(f'Package member mismatch: {name}')
    (destination / 'SHA256SUMS').write_text(''.join(f'{digest}  {name}\n' for name,digest in sorted(checksums.items())))
    (destination / 'context-report.json').write_bytes(json_bytes(report['context']))
    verify_archives(root, version, identity, destination)
    return {'version':version, 'repository':identity, 'packages':checksums, 'same_workshop_content':True, 'reproducible':True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--release', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(build(destination=args.output, release=args.release), indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(1, f'{exc}\n')


if __name__ == '__main__':
    main()
