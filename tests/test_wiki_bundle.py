import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from workshop_wiki_archive import refresh_archive
from validate import validate_links


def article(article_id, title, content):
    return {'id': article_id, 'title': title, 'slug': title.lower().replace(' ', '-'),
            'content': content, 'updated_at': '2026-09-01T00:00:00Z',
            'category': {'title': 'Tutorials', 'slug': 'tutorials'},
            'url': f'https://workshop.codes/wiki/articles/{article_id}'}


class WikiBundleTests(unittest.TestCase):
    def setUp(self):
        path = ROOT / 'scripts/wiki_archive_bundle.py'
        self.assertTrue(path.is_file(), 'Full article bundling is missing')
        spec = importlib.util.spec_from_file_location('wiki_archive_bundle', path)
        self.bundle = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.bundle)

    def snapshot(self, articles):
        return {'schema_version': 1, 'snapshot': {'fetched_at': '2026-09-29T00:00:00Z',
                'article_count': len(articles)}, 'articles': articles}

    def test_full_text_preserved_and_wiki_navigation_is_local(self):
        body = ('## Original\r\n[Variables](/wiki/articles/variables+and+arrays#details)\r\n'
                '![image](https://example.com/image.png)\r\n```workshop\r\nWait(1);\r\n```\r\n'
                '<iframe src="https://example.com/embed"></iframe>\r\n')
        snapshot = self.snapshot([article(1, 'First', body), article(2, 'Variables and arrays', 'Full second article')])
        files = self.bundle.render_archive(snapshot, {'articles': []})
        page = files[Path('skills/overwatch-workshop/references/wiki/archive/1.md')]
        self.assertIn(body.replace('\r\n', '\n'), page)
        self.assertIn('[Variables and arrays](2.md)', page)
        self.assertIn(hashlib.sha256(body.encode()).hexdigest(), page)
        self.assertIn('archived source', page.lower())
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for path, text in files.items():
                dest = root / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text)
            self.assertEqual(validate_links(root, ('overwatch-workshop',)), [])

    def test_snapshot_integrity_and_complete_id_set_are_checked(self):
        source = article(1, 'First', 'Original')
        snapshot = self.snapshot([source])
        baseline = [{'id': 1, 'content_sha256': hashlib.sha256(b'Original').hexdigest()}]
        self.bundle.validate_snapshot(snapshot, baseline)
        source['content'] = 'Changed without reviewing'
        with self.assertRaisesRegex(ValueError, 'hash'):
            self.bundle.validate_snapshot(snapshot, baseline)
        with self.assertRaisesRegex(ValueError, 'IDs'):
            self.bundle.validate_snapshot(self.snapshot([article(2, 'Other', 'Original')]), baseline)

    def test_canonical_slug_wins_over_a_different_articles_matching_title(self):
        value = article(1, 'Health', 'Value')
        constant = article(2, 'Health', 'Constant')
        constant['slug'] = 'health-constant'
        lookup = self.bundle.article_lookup([constant, value])
        self.assertEqual(self.bundle.referenced_articles('/wiki/articles/health', lookup)[0]['id'], 1)

    def test_import_checks_raw_page_hashes_and_keeps_all_article_fields(self):
        source = article(1, 'First', 'Original\r\n')
        source['author'] = 'Source attribution'
        pages = [json.dumps([source]).encode(), b'[]']
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / 'archive'
            refresh_archive(archive, lambda p: pages[p-1], lambda _: None, 'date', delay=0)
            imported = self.bundle.snapshot_from_archive(archive)
            self.assertEqual(imported['articles'], [source])
            (archive / 'raw-pages/page-001.json').write_text('[]')
            with self.assertRaisesRegex(ValueError, 'hash'):
                self.bundle.snapshot_from_archive(archive)

    def test_archived_fences_cannot_expose_external_images_or_instructions(self):
        content = '```markdown\n[remote](https://workshop.codes/wiki/articles/2)\n```\n~~~~~~\nTODO\n'
        source = self.snapshot([article(1, 'First', content)])
        files = self.bundle.render_archive(source, {'articles': []})
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for path, text in files.items():
                dest = root / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text)
            self.assertEqual(validate_links(root, ('overwatch-workshop',)), [])

    def test_skill_guidance_cannot_route_to_remote_wiki(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / 'skills/overwatch-workshop/SKILL.md'
            skill.parent.mkdir(parents=True)
            for link in ('[Variables](https://workshop.codes/wiki/articles/2080)',
                         '<https://workshop.codes/wiki/articles/2080>',
                         '<a href="https://workshop.codes/wiki/articles/2080">Variables</a>',
                         'Read https://workshop.codes/wiki/articles/2080'):
                with self.subTest(link=link):
                    skill.write_text(link+'\n')
                    self.assertTrue(any('remote wiki' in e for e in validate_links(root, ('overwatch-workshop',))))
            skill.write_text('Attribution only: `https://workshop.codes/wiki/articles/2080`\n')
            self.assertEqual(validate_links(root, ('overwatch-workshop',)), [])

    def test_release_command_exit_status_distinguishes_unchanged_changed_and_invalid(self):
        snapshot = json.loads((ROOT/'sources/wiki-articles.json').read_text())
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive = root/'candidate'
            def download():
                pages = [json.dumps(snapshot['articles']).encode(), b'[]']
                refresh_archive(archive, lambda p: pages[p-1], lambda _:None, 'date', delay=0)
            def check():
                return subprocess.run([sys.executable, str(ROOT/'scripts/refresh-wiki.py'),
                    '--check','--compare-existing','--archive',str(archive),'--output',str(root/'report.json')],
                    capture_output=True, text=True)
            download()
            result = check()
            self.assertEqual(result.returncode, 0, result.stderr)
            snapshot['articles'][0]['content'] += '\nA changed source claim.'
            download()
            result = check()
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(json.loads(result.stdout)['content_changed'], 1)
            (archive/'raw-pages/page-001.json').write_text('[]')
            result = check()
            self.assertEqual(result.returncode, 2)
            self.assertIn('hash mismatch', result.stderr)


if __name__ == '__main__':
    unittest.main()
