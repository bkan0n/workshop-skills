#!/usr/bin/env python3
"""Validate portable skill metadata, links, source locks, and corpus accounting."""
import argparse
import hashlib
import json
import math
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('overwatch-workshop', 'overpy')


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def metadata(text):
    """Read our intentionally small YAML subset; reject ambiguous structures."""
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('SKILL.md must start with YAML frontmatter')
    front = text.split('\n---\n', 1)[0][4:]
    result, parent, folded = {}, None, None
    for line in front.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line.startswith(' ') and folded:
            result[folded] = (result[folded] + ' ' + line.strip()).strip()
            continue
        match = re.fullmatch(r'( *)([a-zA-Z0-9_-]+):(?: +(.*))?', line)
        if not match:
            raise ValueError(f'Unsupported frontmatter syntax: {line}')
        indent, key, value = match.groups()
        if not indent:
            parent, folded = None, None
            if value is None:
                if key != 'metadata':
                    raise ValueError(f'Only metadata may contain a map: {key}')
                parent = key
                continue
        elif parent != 'metadata' or len(indent) != 2:
            raise ValueError(f'Unexpected frontmatter nesting: {line}')
        name = f'metadata.{key}' if indent else key
        if name in result:
            raise ValueError(f'Duplicate metadata field: {name}')
        if value in ('>', '|', '>-', '|-'):
            result[name], folded = '', name
        else:
            if value is None:
                raise ValueError(f'Missing metadata value: {name}')
            if value.startswith('"'):
                value = json.loads(value)
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1].replace("''", "'")
            result[name] = value
    return result


def markdown_prose(text):
    """Exclude fenced source, respecting fence character and opening length."""
    result, fence = [], None
    for line in text.splitlines(keepends=True):
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\n'))
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match:
            fence = match[1]
        else:
            result.append(line)
    return ''.join(result)


def markdown_anchors(text):
    text = markdown_prose(text)
    anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']\s*>', text))
    seen = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'<[^>]+>', '', title).lower()
        slug = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        anchors.add(slug + (f'-{count}' if count else ''))
    return anchors


def check_destination(root, target, errors, label):
    file, _, fragment = target.partition('#')
    dest = (root / unquote(file)).resolve()
    if not dest.is_relative_to(root.resolve()) or not dest.is_file():
        errors.append(f'{label}: missing/outside destination {target}')
    elif fragment and dest.suffix == '.md' and unquote(fragment) not in markdown_anchors(dest.read_text()):
        errors.append(f'{label}: missing anchor {target}')


def validate_links(root, skills=SKILLS):
    root = Path(root).resolve()
    errors = []
    skill_root = (root / 'skills').resolve()
    for name in skills:
        for file in (skill_root / name).rglob('*.md'):
            text = file.read_text(encoding='utf-8')
            # Fenced snippets can contain Markdown source that is not a document link.
            prose = markdown_prose(text)
            # Bare URLs, autolinks and HTML anchors can also send a reader online.
            # Inline-code provenance and quoted full article source remain inert.
            navigation = re.sub(r'(`+)(.+?)\1', '', prose, flags=re.S)
            if re.search(r'https?://(?:www\.)?workshop\.codes/wiki(?:/|\b)', navigation, re.I):
                errors.append(f'{file.relative_to(root)}: remote wiki reading link; use a bundled article')
            for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)', prose):
                target = target.strip('<>')
                if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    if not target.startswith(('https://', 'http://', 'mailto:')):
                        errors.append(f'{file.relative_to(root)}: host-specific URI {target}')
                    continue
                path_part, _, anchor = target.partition('#')
                dest = (file.parent / unquote(path_part)).resolve() if path_part else file
                allowed = (skill_root / name).resolve()
                companion = (skill_root / 'overwatch-workshop').resolve()
                if not dest.is_relative_to(allowed) and not (name == 'overpy' and dest.is_relative_to(companion)):
                    errors.append(f'{file.relative_to(root)}: link leaves permitted installed roots: {target}')
                elif not dest.is_file():
                    errors.append(f'{file.relative_to(root)}: missing {target}')
                elif anchor and dest.suffix == '.md' and unquote(anchor) not in markdown_anchors(dest.read_text()):
                    errors.append(f'{file.relative_to(root)}: missing anchor {target}')
            if re.search(r'/Users/|/home/[^ /]+/|[A-Z]:\\Users\\|/private/tmp/', prose):
                errors.append(f'{file.relative_to(root)}: machine-specific path')
            if re.search(r'\b(TODO|TBD|FIXME)\b', prose):
                errors.append(f'{file.relative_to(root)}: unfinished placeholder')
    return errors


def validate_coverage(root):
    errors = []
    corpus = read_json(root / 'sources/wiki-content.json')
    coverage = read_json(root / 'coverage/wiki-coverage.json')
    survey = read_json(root / 'docs/research/workshop-wiki-survey-2026-10-07/article-ledger.json')
    records = corpus['articles']
    by_id = {a['id']: a for a in records}
    if len(by_id) != len(records) or not {a['id'] for a in survey}.issubset(by_id):
        errors.append('Wiki records lose original local IDs or contain duplicates')
    note_ids = set()
    for original in survey:
        article = by_id.get(original['id'], {})
        if article.get('source_content_sha256') != original['source_content_sha256'] and not article.get('source_backed'):
            errors.append(f"wiki-{original['id']}: changed source still uses old extracted claims")
        notes = article.get('notes', [])
        wanted = {f"wiki-{original['id']}-n{i}" for i in range(1, len(original['important_information']) + 1)}
        actual = {n['id'] for n in notes}
        if wanted != actual or len(actual) != len(notes):
            errors.append(f"wiki-{original['id']}: missing or duplicate survey notes")
    snapshot_path = root / 'sources/wiki-articles.json'
    if snapshot_path.is_file():
        from wiki_archive_bundle import content_hash
        current = {a['id']: a for a in read_json(snapshot_path)['articles']}
        matched = []
        for article in records:
            revision = article.get('source_revision_id', article['id'])
            if article.get('source_missing'):
                if revision in current or not article.get('source_backed'):
                    errors.append(f"wiki-{article['id']}: invalid removed article state")
                continue
            matched.append(revision)
            if revision not in current or content_hash(current[revision]) != article['source_content_sha256']:
                errors.append(f"wiki-{article['id']}: source hash/revision differs from installed snapshot")
        if len(matched) != len(set(matched)) or set(matched) != set(current):
            errors.append('Wiki records must account for every current source article exactly once')
    for article in records:
        notes = article.get('notes', [])
        if not article.get('disposition'):
            errors.append(f"wiki-{article['id']}: missing disposition")
        for note in notes:
            if note['id'] in note_ids:
                errors.append(f"Duplicate claim {note['id']}")
            note_ids.add(note['id'])
            if not note.get('text') or not note.get('evidence_status'):
                errors.append(f"{note['id']}: missing assertion/evidence")
            if note.get('destination'):
                check_destination(root, note['destination'], errors, note['id'])
            elif not (note.get('reason') or article.get('reason')):
                errors.append(f"{note['id']}: no destination or explicit exclusion/defer reason")
    # Generator checks full serialized coverage; here independently require its ID set.
    coverage_records = coverage['articles']
    if len(coverage_records) != len(by_id) or {x['id'] for x in coverage_records} != set(by_id):
        errors.append('Coverage ledger does not account for every local article record')
    return errors, {'articles': len(records), 'notes': len(note_ids)}


def context_report(root):
    required = [root / 'skills' / name / file for name in SKILLS for file in ('SKILL.md', 'references/foundation.md')]
    rows = []
    for file in required:
        text = file.read_text(encoding='utf-8')
        rows.append({'path': file.relative_to(root).as_posix(), 'characters': len(text), 'words': len(text.split()), 'estimated_tokens': math.ceil(len(text)/4)})
    native = sum(x['estimated_tokens'] for x in rows[:2])
    combined = sum(x['estimated_tokens'] for x in rows)
    large = []
    for file in sorted((root / 'skills').rglob('*.md')):
        size = math.ceil(len(file.read_text()) / 4)
        if size > 3000:
            large.append({'path': file.relative_to(root).as_posix(), 'estimated_tokens': size})
    return {'method': 'ceil(Unicode characters / 4); estimate, not a model tokenizer', 'required_files': rows,
            'workshop_estimate': native, 'combined_estimate': combined, 'targets': {'workshop':2500,'combined':4500},
            'within_targets': native <= 2500 and combined <= 4500, 'large_selective_references': large}


def validate(root=ROOT):
    root = Path(root).resolve()
    errors, versions = [], {}
    expected = read_json(root / 'package.json')['version']
    for name in SKILLS:
        file = root / 'skills' / name / 'SKILL.md'
        try:
            fields = metadata(file.read_text())
            if fields.get('name') != name or len(name) > 64:
                errors.append(f'{name}: invalid skill name')
            if not 1 <= len(fields.get('description', '')) <= 1024:
                errors.append(f'{name}: description must contain 1–1024 characters')
            version = fields.get('metadata.workshop-skills-version')
            versions[name] = version
            if version != expected:
                errors.append(f'{name}: skill version {version} differs from package {expected}')
            if name == 'overpy' and fields.get('metadata.workshop-skills-requires-workshop') != expected:
                errors.append('OverPy companion version mismatch')
        except (ValueError, OSError) as exc:
            errors.append(f'{name}: {exc}')
    errors.extend(validate_links(root))
    try:
        more, counts = validate_coverage(root)
        errors.extend(more)
    except (ValueError, KeyError, OSError) as exc:
        errors.append(f'Corpus records invalid: {exc}')
        counts = {}
    lock = read_json(root / 'sources/lock.json')
    if lock['release'] != expected:
        errors.append('Release version and source lock disagree')
    if sha256(root / 'sources/wiki-index.json') != lock['wiki']['index_sha256']:
        errors.append('Wiki source index hash mismatch')
    try:
        from wiki_archive_bundle import validate_snapshot
        snapshot = read_json(root / 'sources/wiki-articles.json')
        validate_snapshot(snapshot, read_json(root / 'sources/wiki-index.json'))
        if sha256(root / 'sources/wiki-articles.json') != lock['wiki'].get('articles_sha256'):
            errors.append('Full wiki source snapshot hash mismatch')
        archived = root / 'skills/overwatch-workshop/references/wiki/archive'
        expected_ids = {str(a['id']) for a in snapshot['articles']}
        for article in read_json(root / 'sources/wiki-content.json')['articles']:
            expected_ids.update(str(i) for i in article.get('revision_ids', [article['id']]))
        if {p.stem for p in archived.glob('[0-9]*.md')} != expected_ids:
            errors.append('Installed full wiki articles differ from the source snapshot IDs')
    except (KeyError, ValueError, OSError) as exc:
        errors.append(f'Full wiki archive invalid: {exc}')
    package_lock = read_json(root / 'package-lock.json')
    if package_lock.get('version') != expected or package_lock['packages'][''].get('version') != expected:
        errors.append('Root package-lock versions disagree with package version')
    npm = package_lock['packages']['node_modules/overpy']
    snapshot = read_json(root / 'sources/overpy-api.json')
    if npm['version'] != lock['overpy']['version'] or npm['integrity'] != lock['overpy']['package_integrity']:
        errors.append('OverPy dependency lock disagrees with source lock')
    if snapshot['source_commit'] != lock['overpy']['commit'] or snapshot['package_integrity'] != npm['integrity']:
        errors.append('OverPy normalized snapshot identity mismatch')
    if sha256(root / 'sources/overpy-api.json') != lock['overpy']['snapshot_sha256']:
        errors.append('OverPy normalized snapshot hash mismatch')
    context = context_report(root)
    return {'ok': not errors, 'errors': errors, 'versions': versions, 'coverage': counts, 'context': context}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    report = validate()
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report['ok'] else 1)


if __name__ == '__main__':
    main()
