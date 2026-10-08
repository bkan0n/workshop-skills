"""Apply a trusted wiki snapshot and regenerate references transactionally."""
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from wiki_archive_bundle import content_hash, validate_snapshot

REPLACED = ('sources', 'skills', 'coverage')


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def synchronize_sources(root, candidate):
    previous = read(root/'sources/wiki-articles.json')
    corpus = read(root/'sources/wiki-content.json')
    old = {a['id']: a for a in previous['articles']}
    current = {a['id']: a for a in candidate['articles']}
    groups = {a['group_id']: a for a in candidate['articles'] if a.get('group_id')}
    group_ids = [a['group_id'] for a in candidate['articles'] if a.get('group_id')]
    if len(groups) != len(group_ids):
        raise ValueError('Ambiguous wiki article group identities')
    matched = set()
    for record in corpus['articles']:
        revision = record.get('source_revision_id', record['id'])
        previous_article = old.get(revision, {})
        record['source_slugs'] = sorted(set(record.get('source_slugs', [])) | ({previous_article['slug']} if previous_article else set()))
        group = record.get('source_group_id') or previous_article.get('group_id')
        article = current.get(revision) or groups.get(group)
        record['revision_ids'] = sorted(set(record.get('revision_ids', [])) | {record['id'], revision})
        if group:
            record['source_group_id'] = group
        if article is None:
            record['source_missing'] = True
            record['source_backed'] = True
            record['disposition'] = 'removed'
        else:
            if article['id'] in matched:
                raise ValueError('Multiple local records match one current wiki article')
            matched.add(article['id'])
            changed = record['source_content_sha256'] != content_hash(article) or record.get('source_missing')
            record['source_revision_id'] = article['id']
            record['source_group_id'] = article.get('group_id')
            record['source_slugs'] = sorted(set(record['source_slugs']) | {article['slug']})
            record['revision_ids'] = sorted(set(record['revision_ids']) | {article['id']})
            record['source_missing'] = False
            record.update(title=article['title'], source_url=article['url'],
                          source_updated_at=article['updated_at'], source_content_sha256=content_hash(article),
                          category=article['category']['title'])
            if changed or record.get('source_backed'):
                record['source_backed'] = True
                record['disposition'] = 'source'
        if record.get('source_backed'):
            record['review_status'] = 'synced'
            record['reason'] = 'Generated directly from the trusted wiki source.'
            record['destination'] = f"skills/overwatch-workshop/references/wiki/articles/{record['id']}.md#wiki-{record['id']}"
            record['uncertainties'] = []
            record.pop('api_summary', None)
            record.pop('omitted_material', None)
            # Keep stable claim anchors used by guides and examples, while replacing
            # obsolete summaries with the current source text at their destination.
            for note in record['notes']:
                note.update(text='Current wiki source is included at this article destination.',
                            evidence_status='wiki-documentation', uncertainty=[],
                            source_location=['Current article text'], disposition='source',
                            destination=record['destination'].split('#')[0]+'#'+note['id'])
    additions = [a for a in candidate['articles'] if a['id'] not in matched]
    if additions:
        corpus['topics']['updates'] = {'title':'New wiki articles', 'read_when':'Read for newly added wiki documentation.'}
    for article in additions:
        corpus['articles'].append({
            'id':article['id'], 'source_revision_id':article['id'], 'source_group_id':article.get('group_id'),
            'revision_ids':[article['id']], 'source_slugs':[article['slug']], 'title':article['title'], 'source_url':article['url'],
            'source_updated_at':article['updated_at'], 'source_content_sha256':content_hash(article),
            'category':article['category']['title'], 'disposition':'source', 'source_backed':True,
            'reason':'Generated directly from the trusted wiki source.', 'topics':['wiki updates'], 'topic':'updates',
            'source_location':f"API article {article['id']}", 'review_status':'synced', 'uncertainties':[], 'notes':[],
            'tables':[], 'destination':f"skills/overwatch-workshop/references/wiki/articles/{article['id']}.md#wiki-{article['id']}"})
    by_id = {a['id']: a for a in corpus['articles']}
    for path in (root/'sources/wiki-tables').glob('*.json'):
        table = read(path)
        article = by_id[table['source_article_id']]
        if not article.get('source_backed'):
            continue
        table['source_backed'] = True
        table['context'] = []
        table['evidence_status'] = 'wiki-documentation'
        # Preserve destinations/anchors, not copied rows from an older revision.
        for part in table['tables']:
            part['columns'], part['rows'] = [], []
        write(path, table)
    corpus['snapshot'].update(date=candidate['snapshot']['fetched_at'], article_count=len(corpus['articles']),
                              active_article_count=len(candidate['articles']),
                              survey_note_count=sum(len(a['notes']) for a in corpus['articles']))
    write(root/'sources/wiki-content.json',corpus)
    write(root/'sources/wiki-articles.json',candidate)
    index = [{k:a[k] for k in ('id','title','slug','url','updated_at')} |
             {'category':a['category']['title'],'content_sha256':content_hash(a)} for a in candidate['articles']]
    write(root/'sources/wiki-index.json',index)
    lock = read(root/'sources/lock.json')
    lock['wiki'].update(snapshot=candidate['snapshot']['fetched_at'], article_count=len(candidate['articles']),
                        information_note_count=corpus['snapshot']['survey_note_count'], snapshot_complete=True)
    for key in ('populated_pages', 'first_empty_page'):
        if key in candidate['snapshot']:
            lock['wiki'][key] = candidate['snapshot'][key]
    for filename, key in [('wiki-index.json','index_sha256'),('wiki-articles.json','articles_sha256')]:
        lock['wiki'][key] = hashlib.sha256((root/'sources'/filename).read_bytes()).hexdigest()
    write(root/'sources/lock.json',lock)


def tree_hashes(root):
    return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
            for name in REPLACED for p in (root/name).rglob('*') if p.is_file()}


def apply_snapshot(root, candidate):
    """Validate a staged regeneration before replacing any installed directory."""
    root = Path(root).resolve()
    validate_snapshot(candidate)
    originals = tree_hashes(root)
    cache = root/'.cache'
    cache.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='wiki-update-',dir=cache) as temp:
        stage = Path(temp)/'stage'
        stage.mkdir()
        for name in (*REPLACED,'scripts'):
            shutil.copytree(root/name,stage/name,ignore=shutil.ignore_patterns('__pycache__'))
        ledger=Path('docs/research/workshop-wiki-survey-2026-10-07/article-ledger.json')
        (stage/ledger).parent.mkdir(parents=True)
        shutil.copyfile(root/ledger,stage/ledger)
        for name in ('package.json','package-lock.json'):
            shutil.copyfile(root/name,stage/name)
        synchronize_sources(stage,copy.deepcopy(candidate))
        for command in ([sys.executable,'scripts/generate-wiki.py'],['node','scripts/generate-api.mjs'],
                        [sys.executable,'scripts/validate.py']):
            result = subprocess.run(command,cwd=stage,text=True,capture_output=True)
            if result.returncode:
                raise ValueError('Wiki update generation/validation failed: '+(result.stdout+result.stderr).strip())
        if tree_hashes(root) != originals:
            raise ValueError('Files changed during wiki update; retry with the latest checkout')
        backup = Path(temp)/'backup'
        backup.mkdir()
        moved = []
        try:
            for name in REPLACED:
                os.replace(root/name,backup/name)
                moved.append(name)
                os.replace(stage/name,root/name)
        except OSError:
            for name in reversed(moved):
                if (root/name).exists():
                    shutil.rmtree(root/name)
                os.replace(backup/name,root/name)
            raise
