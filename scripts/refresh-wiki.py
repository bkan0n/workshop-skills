#!/usr/bin/env python3
"""Fetch trusted wiki articles through the JSON API and update local skills."""
import argparse
from collections import Counter
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from validate import ROOT, read_json
from workshop_wiki_archive import refresh_archive, fetch_live_page
from wiki_archive_bundle import snapshot_from_archive, validate_snapshot, content_hash, BASE
from wiki_update import apply_snapshot


def comparison_index(snapshot):
    """Keep stable article identity and detect changes to any supplied metadata."""
    result = []
    for article in snapshot['articles']:
        metadata = {k: v for k, v in article.items() if k != 'content'}
        row = {k: article[k] for k in ('id','title','url','updated_at','slug','tags','group_id') if k in article}
        row.update(category=article['category']['title'], content_sha256=content_hash(article),
                   metadata_sha256=hashlib.sha256(json.dumps(metadata,sort_keys=True,ensure_ascii=False).encode()).hexdigest())
        result.append(row)
    return result


def compare_snapshots(baseline, current, corpus, snapshot, tables=()):
    if not snapshot.get('article_count') or snapshot['article_count'] != len(current):
        raise ValueError('Snapshot article count is incomplete or inconsistent')
    if snapshot.get('first_empty_page') != snapshot.get('populated_pages', -1) + 1:
        raise ValueError('Snapshot has no validated terminal empty page')
    if len({x['id'] for x in current}) != len(current):
        raise ValueError('Snapshot has duplicate IDs')
    old={x['id']:x for x in baseline};new={x['id']:x for x in current}
    if len(old) != len(baseline):
        raise ValueError('Baseline has duplicate IDs')
    for rows in (baseline, current):
        groups = [x['group_id'] for x in rows if x.get('group_id')]
        if len(groups) != len(set(groups)):
            raise ValueError('Snapshot has ambiguous article group identities')
    new_groups = {x['group_id']: x for x in current if x.get('group_id')}
    pairs, matched = [], set()
    for before in baseline:
        after = new.get(before['id']) or new_groups.get(before.get('group_id'))
        if after:
            if after['id'] in matched:
                raise ValueError('Ambiguous revision match')
            matched.add(after['id'])
        pairs.append((before, after))
    pairs += [(None, after) for after in current if after['id'] not in matched]
    affected={a['id']:({n['destination'] for n in a.get('notes',[]) if n.get('destination')} |
                       {a[k] for k in ('destination','catalog_destination') if a.get(k)} |
                       set(a.get('tables', [])) |
                       {d for n in a.get('notes',[]) for d in n.get('related_destinations',[])}) for a in corpus['articles']}
    for table in tables:
        affected.setdefault(table['source_article_id'],set()).update(
            [table['destination'], *[t['destination'] for t in table['tables'] if t.get('destination')]])
    for article in corpus['articles']:
        affected.setdefault(article.get('source_revision_id',article['id']),set()).update(affected[article['id']])
    result=[]
    for before, after in sorted(pairs, key=lambda pair: (pair[1] or pair[0])['id']):
        article_id = (after or before)['id']
        changed_fields=[key for key in ('id','content_sha256','title','category','url','updated_at','slug','tags','group_id','metadata_sha256') if before and after and before.get(key)!=after.get(key)]
        change='added' if before is None else 'missing-from-complete-snapshot' if after is None else 'changed' if changed_fields else None
        if change:
            references = affected.get(article_id, set()) | {str(BASE / f'{article_id}.md')}
            if before:
                references |= affected.get(before['id'], set()) | {str(BASE / f"{before['id']}.md")}
            result.append({'id':article_id,'change':change,'title':(after or before)['title'],
                           'previous_id':before['id'] if before else None,
                           'previous_hash':before['content_sha256'] if before else None,
                           'current_hash':after['content_sha256'] if after else None,
                           'changed_fields':changed_fields,
                           'content_changed': bool(before and after and before['content_sha256'] != after['content_sha256']),
                           'affected_references':sorted(references),
                           'action':'Replace local source and regenerate references from trusted wiki text.'})
    counts = Counter(item['change'] for item in result)
    return {'snapshot':snapshot['fetched_at'],'complete':True,'changes':result,
            'summary': {'added':counts['added'],'changed':counts['changed'],
                        'missing':counts['missing-from-complete-snapshot'],
                        'content_changed':sum(item['content_changed'] for item in result)},
            'applied':False,'curated_files_modified':False,'installed_files_modified':False}


def check_wiki(root=ROOT, archive=None, output=None, compare_existing=False,
               fetch_page=fetch_live_page, pause=time.sleep):
    """Download a candidate, verify its bytes, and report changes without promotion."""
    root = Path(root)
    archive = Path(archive or root/'.cache/wiki-candidate')
    output = Path(output or root/'.cache/wiki-update-report.json')
    if not compare_existing:
        timestamp=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
        refresh_archive(archive,fetch_page,pause,timestamp,delay=3)
    candidate = snapshot_from_archive(archive)
    installed = read_json(root/'sources/wiki-articles.json')
    validate_snapshot(installed,read_json(root/'sources/wiki-index.json'))
    queue=compare_snapshots(comparison_index(installed),comparison_index(candidate),
                       read_json(root/'sources/wiki-content.json'),read_json(archive/'manifest.json'),
                       [read_json(p) for p in sorted((root/'sources/wiki-tables').glob('*.json'))])
    output.parent.mkdir(parents=True,exist_ok=True)
    candidate_path = output.with_name('wiki-articles.candidate.json')
    candidate_path.write_text(json.dumps(candidate,ensure_ascii=False,indent=2)+'\n')
    queue['candidate_source'] = str(candidate_path)
    output.write_text(json.dumps(queue,ensure_ascii=False,indent=2)+'\n')
    return queue


def update_wiki(root=ROOT, output=None, **kwargs):
    """Apply changed source automatically after staged file/link validation."""
    output = Path(output or Path(root)/'.cache/wiki-update-report.json')
    report = check_wiki(root=root,output=output,**kwargs)
    if report['changes']:
        apply_snapshot(root,read_json(Path(report['candidate_source'])))
        report.update(applied=True,curated_files_modified=True,installed_files_modified=True)
        output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    return report


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',type=Path,default=ROOT/'.cache/wiki-candidate')
    parser.add_argument('--compare-existing',action='store_true',help='Compare a previously completed local API snapshot without fetching')
    parser.add_argument('--output',type=Path,default=ROOT/'.cache/wiki-update-report.json')
    parser.add_argument('--check',action='store_true',help='Check only: write no installed files; exit 1 for changes, 0 if unchanged.')
    args=parser.parse_args(argv)
    try:
        operation = check_wiki if args.check else update_wiki
        queue=operation(archive=args.archive,output=args.output,compare_existing=args.compare_existing)
    except (KeyError, ValueError, OSError) as exc:
        parser.exit(2, f'Wiki maintenance failed; installed sources were not modified: {exc}\n')
    print(json.dumps({'update_report':str(args.output),'candidate_source':queue['candidate_source'],
                      'changes':len(queue['changes']),**queue['summary'],'applied':queue['applied'],
                      'installed_files_modified':queue['installed_files_modified']},indent=2))
    return 1 if args.check and queue['changes'] else 0


if __name__=='__main__':
    raise SystemExit(main())
