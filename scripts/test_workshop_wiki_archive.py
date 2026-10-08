import json
import tempfile
import unittest
from pathlib import Path

from workshop_wiki_archive import refresh_archive


def article(article_id, title, category="Actions"):
    return {
        "id": article_id,
        "title": title,
        "subtitle": None,
        "content": "## Description\r\n\r\nExample content.\r\n",
        "slug": title.lower().replace(" ", "-"),
        "tags": "example, test",
        "category_id": 7,
        "group_id": "example",
        "created_at": "2026-09-01T00:00:00.000Z",
        "updated_at": "2026-09-02T00:00:00.000Z",
        "category": {"id": 7, "title": category, "slug": category.lower()},
        "url": f"https://workshop.codes/wiki/articles/{article_id}",
    }


def json_bytes(items):
    return json.dumps(items, ensure_ascii=False).encode("utf-8")


class ArchiveTests(unittest.TestCase):
    def test_writes_source_linked_markdown_index_and_original_page_bytes(self):
        first = json_bytes([article(101, "Start Scaling Player")])
        responses = [first, b"[]"]
        calls = []
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "wiki"
            refresh_archive(target, lambda page: (calls.append(page), responses[page - 1])[1],
                            lambda seconds: None, "2026-09-28T00:00:00Z", delay=0)

            self.assertEqual(calls, [1, 2])
            self.assertEqual((target / "raw-pages" / "page-001.json").read_bytes(), first)
            index = json.loads((target / "index.json").read_text())
            self.assertEqual(index[0]["title"], "Start Scaling Player")
            self.assertEqual(index[0]["category"], "Actions")
            self.assertEqual(index[0]["tags"], ["example", "test"])
            markdown = (target / index[0]["path"]).read_text()
            self.assertIn("# Start Scaling Player", markdown)
            self.assertIn("https://workshop.codes/wiki/articles/101", markdown)
            self.assertIn("Example content.", markdown)
            manifest = json.loads((target / "manifest.json").read_text())
            self.assertEqual(manifest["article_count"], 1)
            self.assertEqual(manifest["populated_pages"], 1)
            self.assertEqual(manifest["first_empty_page"], 2)

    def test_rejects_duplicate_ids_without_replacing_existing_archive(self):
        duplicate = json_bytes([article(101, "First"), article(101, "Second")])
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "wiki"
            target.mkdir()
            (target / "sentinel.txt").write_text("keep")
            with self.assertRaisesRegex(ValueError, "duplicate"):
                refresh_archive(target, lambda page: duplicate, lambda seconds: None,
                                "2026-09-28T00:00:00Z", delay=0, max_pages=1)
            self.assertEqual((target / "sentinel.txt").read_text(), "keep")

    def test_rejects_missing_required_fields(self):
        incomplete = article(101, "Incomplete")
        del incomplete["content"]
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "content"):
                refresh_archive(Path(temp) / "wiki", lambda page: json_bytes([incomplete]),
                                lambda seconds: None, "2026-09-28T00:00:00Z",
                                delay=0, max_pages=1)

    def test_resolves_site_relative_markdown_links(self):
        linked = article(101, "Linked")
        linked["content"] = "See [Player](/wiki/articles/player) and ![icon](/images/icon.png)."
        responses = [json_bytes([linked]), b"[]"]
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "wiki"
            refresh_archive(target, lambda page: responses[page - 1],
                            lambda seconds: None, "2026-09-28T00:00:00Z", delay=0)
            path = json.loads((target / "index.json").read_text())[0]["path"]
            markdown = (target / path).read_text()
            self.assertIn("[Player](https://workshop.codes/wiki/articles/player)", markdown)
            self.assertIn("![icon](https://workshop.codes/images/icon.png)", markdown)

    def test_stops_at_first_empty_page_and_waits_between_requests(self):
        responses = [json_bytes([article(1, "One")]), json_bytes([article(2, "Two")]), b"[]"]
        requested = []
        pauses = []
        with tempfile.TemporaryDirectory() as temp:
            refresh_archive(Path(temp) / "wiki",
                            lambda page: (requested.append(page), responses[page - 1])[1],
                            pauses.append, "2026-09-28T00:00:00Z", delay=3)
        self.assertEqual(requested, [1, 2, 3])
        self.assertEqual(pauses, [3, 3])

    def test_fetch_failure_keeps_previous_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "wiki"
            target.mkdir()
            (target / "sentinel.txt").write_text("keep")

            def fetch(page):
                if page == 1:
                    return json_bytes([article(1, "One")])
                raise OSError("network failure")

            with self.assertRaisesRegex(OSError, "network failure"):
                refresh_archive(target, fetch, lambda seconds: None,
                                "2026-09-28T00:00:00Z", delay=0)
            self.assertEqual((target / "sentinel.txt").read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
