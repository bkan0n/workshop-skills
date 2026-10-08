#!/usr/bin/env python3
"""Fetch through the wiki API and queue source changes without rewriting skills."""
import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from validate import ROOT, read_json
from workshop_wiki_archive import refresh_archive, fetch_live_page


def review_queue(baseline, current, corpus, snapshot, tables=()):
    if not snapshot.get('article_count') or snapshot['article_count'] != len(current):
        raise ValueError('Snapshot article count is incomplete or inconsistent')
    if snapshot.get('first_empty_page') != snapshot.get('populated_pages', -1) + 1:
        raise ValueError('Snapshot has no validated terminal empty page')
    if len({x['id'] for x in current}) != len(current):
        raise ValueError('Snapshot has duplicate IDs')
    old={x['id']:x for x in baseline};new={x['id']:x for x in current}
    affected={a['id']:({n['destination'] for n in a.get('notes',[]) if n.get('destination')} |
                       {a[k] for k in ('destination','catalog_destination') if a.get(k)} |
                       set(a.get('tables', [])) |
                       {d for n in a.get('notes',[]) for d in n.get('related_destinations',[])}) for a in corpus['articles']}
    for table in tables:
        affected.setdefault(table['source_article_id'],set()).update(
            [table['destination'], *[t['destination'] for t in table['tables'] if t.get('destination')]])
    result=[]
    for article_id in sorted(old.keys() | new.keys()):
        before,after=old.get(article_id),new.get(article_id)
        changed_fields=[key for key in ('content_sha256','title','category','url','updated_at') if before and after and before.get(key)!=after.get(key)]
        change='added' if before is None else 'missing-from-complete-snapshot' if after is None else 'changed' if changed_fields else None
        if change:
            result.append({'id':article_id,'change':change,'title':(after or before)['title'],
                           'previous_hash':before['content_sha256'] if before else None,
                           'current_hash':after['content_sha256'] if after else None,
                           'changed_fields':changed_fields,
                           'references_to_review':sorted(affected.get(article_id,set())),
                           'decision':'Review source and affected claims; do not overwrite curated content automatically.'})
    return {'snapshot':snapshot['fetched_at'],'complete':True,'changes':result,'curated_files_modified':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',type=Path,default=ROOT/'archive')
    parser.add_argument('--compare-existing',action='store_true',help='Compare a previously completed local API snapshot without fetching')
    parser.add_argument('--output',type=Path,default=ROOT/'.cache/wiki-review-queue.json')
    args=parser.parse_args()
    if not args.compare_existing:
        timestamp=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
        refresh_archive(args.archive,fetch_live_page,time.sleep,timestamp,delay=3)
    queue=review_queue(read_json(ROOT/'sources/wiki-index.json'),read_json(args.archive/'index.json'),
                       read_json(ROOT/'sources/wiki-content.json'),read_json(args.archive/'manifest.json'),
                       [read_json(p) for p in sorted((ROOT/'sources/wiki-tables').glob('*.json'))])
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(queue,indent=2)+'\n')
    print(json.dumps({'review_queue':str(args.output),'changes':len(queue['changes']),'curated_files_modified':False}))


if __name__=='__main__':
    main()
