import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))


class WikiUpdateTests(unittest.TestCase):
    def setUp(self):
        path = ROOT/'scripts/wiki_update.py'
        self.assertTrue(path.is_file(), 'Automatic wiki updates are missing')
        spec = importlib.util.spec_from_file_location('wiki_update', path)
        self.update = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.update)
        self.snapshot = json.loads((ROOT/'sources/wiki-articles.json').read_text())

    def fixture(self, root):
        for name in ('sources','skills','coverage','scripts'):
            shutil.copytree(ROOT/name, root/name, ignore=shutil.ignore_patterns('__pycache__'))
        ledger = Path('docs/research/workshop-wiki-survey-2026-10-07/article-ledger.json')
        (root/ledger).parent.mkdir(parents=True)
        shutil.copyfile(ROOT/ledger,root/ledger)
        for name in ('package.json','package-lock.json'):
            shutil.copyfile(ROOT/name,root/name)

    def test_apply_updates_source_hashes_generated_notes_and_tables_with_stable_links(self):
        candidate = copy.deepcopy(self.snapshot)
        record = next(a for a in candidate['articles'] if a['slug']=='ow2-workshop-changesbugs')
        record['id'] = 999999
        record['url'] = 'https://workshop.codes/wiki/articles/999999'
        record['content'] = '# Reading Event Ability\nHeroes not listed work fine.\n\n| Hero | Button |\n| --- | --- |\n| Venture | Primary Fire |\n'
        record['updated_at'] = '2026-10-08T00:00:00Z'
        candidate['snapshot']['fetched_at'] = '2026-10-08T00:00:00Z'
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.fixture(root)
            self.update.apply_snapshot(root,candidate)
            source=json.loads((root/'sources/wiki-articles.json').read_text())
            self.assertTrue(any(a['id']==999999 for a in source['articles']))
            corpus=json.loads((root/'sources/wiki-content.json').read_text())
            article=next(a for a in corpus['articles'] if a['id']==9463)
            self.assertEqual(article['source_revision_id'],999999)
            self.assertTrue(article['source_backed'])
            note=(root/'skills/overwatch-workshop/references/wiki/articles/9463.md').read_text()
            table=(root/'skills/overwatch-workshop/references/wiki/tables/9463.md').read_text()
            self.assertIn('Venture | Primary Fire',note)
            self.assertIn('Venture | Primary Fire',table)
            self.assertNotIn('Kiriko',table)
            self.assertNotIn('Roadhog',note)
            self.assertIn('wiki-9463-n21',note)
            self.assertTrue((root/'skills/overwatch-workshop/references/wiki/archive/9463.md').is_file())
            self.assertTrue((root/'skills/overwatch-workshop/references/wiki/archive/999999.md').is_file())
            # Applying exactly the same source again leaves deterministic output.
            before=(root/'sources/lock.json').read_bytes()
            self.update.apply_snapshot(root,candidate)
            self.assertEqual((root/'sources/lock.json').read_bytes(),before)

    def test_generator_failure_keeps_all_installed_directories_unchanged(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.fixture(root)
            # Force a validation failure in the candidate, after rendering.
            (root/'skills/overwatch-workshop/SKILL.md').write_text('Invalid metadata')
            originals={name:(root/name).read_bytes() for name in (
                'sources/wiki-articles.json','sources/lock.json','coverage/wiki-coverage.json',
                'skills/overwatch-workshop/SKILL.md')}
            with self.assertRaisesRegex(ValueError,'validation'):
                self.update.apply_snapshot(root,self.snapshot)
            for name,content in originals.items():
                self.assertEqual((root/name).read_bytes(),content,name)

    def test_default_maintenance_applies_a_complete_snapshot_without_review(self):
        from workshop_wiki_archive import refresh_archive
        candidate=copy.deepcopy(self.snapshot)
        candidate['articles'][0]['content'] += '\nAutomatically refreshed wiki text.'
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.fixture(root)
            archive=root/'.cache/wiki-candidate'
            pages=[json.dumps(candidate['articles']).encode(),b'[]']
            refresh_archive(archive,lambda page:pages[page-1],lambda _:None,'2026-10-08T00:00:00Z',delay=0)
            result=subprocess.run([sys.executable,'scripts/refresh-wiki.py','--compare-existing'],
                                  cwd=root,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
            report=json.loads((root/'.cache/wiki-update-report.json').read_text())
            self.assertTrue(report['applied'])
            self.assertEqual(report['summary']['content_changed'],1)
            installed=json.loads((root/'sources/wiki-articles.json').read_text())
            self.assertEqual(installed['articles'],candidate['articles'])

    def test_new_and_removed_articles_are_routed_without_broken_old_links(self):
        candidate=copy.deepcopy(self.snapshot)
        removed=candidate['articles'].pop(next(i for i,a in enumerate(candidate['articles']) if a['id']==9562))
        new=copy.deepcopy(candidate['articles'][0])
        new.update(id=999998,group_id='new-identity',slug='brand-new-wiki-article',title='New wiki article',
                   url='https://workshop.codes/wiki/articles/999998',content='New authoritative content.')
        candidate['articles'].append(new)
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.fixture(root)
            self.update.apply_snapshot(root,candidate)
            new_page=root/'skills/overwatch-workshop/references/wiki/articles/999998.md'
            self.assertIn('New authoritative content.',new_page.read_text())
            old_page=root/f"skills/overwatch-workshop/references/wiki/archive/{removed['id']}.md"
            self.assertIn('no longer present',old_page.read_text())
            self.assertNotIn(removed['content'].strip(),old_page.read_text())
            self.assertIn('New wiki article',(root/'skills/overwatch-workshop/references/wiki/updates.md').read_text())

    def test_renamed_source_slug_keeps_pinned_compiler_links_local(self):
        candidate=copy.deepcopy(self.snapshot)
        article=next(a for a in candidate['articles'] if a['id']==9562)
        article.update(id=999997,slug='renamed-texture-reference')
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.fixture(root)
            self.update.apply_snapshot(root,candidate)
            page=(root/'skills/overpy/references/api/constants/texture.md').read_text()
            self.assertIn('wiki/archive/999997.md',page)

    def test_updated_tables_keep_source_conditions_and_split_pages_stay_selective(self):
        candidate=copy.deepcopy(self.snapshot)
        for article in candidate['articles']:
            if article['id'] in (9331,1976,4480):
                article['content'] += '\nUpdated source note outside the table.'
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            self.fixture(root)
            self.update.apply_snapshot(root,candidate)
            article=next(a for a in candidate['articles'] if a['id']==9331)
            table=(root/'skills/overwatch-workshop/references/wiki/tables/9331.md').read_text()
            self.assertIn(article['content'].replace('\r\n','\n'),table)
            part=(root/'skills/overwatch-workshop/references/wiki/tables/1976/control-ilios-well.md').read_text()
            self.assertLess(len(part),1500)
            self.assertIn('Ilios',part)
            self.assertIn('../1976.md',part)
            guide=(root/'skills/overwatch-workshop/references/waits.md').read_text()
            self.assertIn('## Current wiki sources',guide)
            self.assertIn('wiki/archive/4480.md',guide)


if __name__=='__main__':
    unittest.main()
