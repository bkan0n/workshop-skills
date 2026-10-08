#!/usr/bin/env python3
"""Archive the Workshop.codes wiki JSON API for local reference lookup."""

import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


API_URL = "https://workshop.codes/wiki/articles/page/{}.json"
ARTICLE_URL_PREFIX = "https://workshop.codes/wiki/articles/"
REQUIRED_FIELDS = ("id", "title", "slug", "content", "updated_at", "category", "url")


def safe_name(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "untitled"


def validate_article(item, seen_ids):
    if not isinstance(item, dict):
        raise ValueError("article must be a JSON object")
    for field in REQUIRED_FIELDS:
        if field not in item:
            raise ValueError(f"article missing {field}")
    article_id = item["id"]
    if not isinstance(article_id, int) or isinstance(article_id, bool) or article_id <= 0:
        raise ValueError(f"invalid article id: {article_id!r}")
    if article_id in seen_ids:
        raise ValueError(f"duplicate article id: {article_id}")
    seen_ids.add(article_id)
    if not all(isinstance(item[key], str) for key in ("title", "slug", "content", "updated_at", "url")):
        raise ValueError(f"article {article_id} has invalid text fields")
    if not item["url"].startswith(ARTICLE_URL_PREFIX):
        raise ValueError(f"article {article_id} has invalid source URL")
    category = item["category"]
    if not isinstance(category, dict) or not isinstance(category.get("title"), str) or not isinstance(category.get("slug"), str):
        raise ValueError(f"article {article_id} has invalid category")


def fetch_live_page(page):
    request = urllib.request.Request(
        API_URL.format(page),
        headers={"User-Agent": "OverPy-Workshop-Wiki-Archive/1.0 (local reference)"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(3 * (attempt + 1))
    raise RuntimeError("unreachable")


def write_snapshot(staging, pages, fetched_at, first_empty_page):
    raw_dir = staging / "raw-pages"
    raw_dir.mkdir(parents=True)
    articles_dir = staging / "articles"
    articles_dir.mkdir()
    index = []
    category_counts = Counter()
    page_hashes = {}

    for page_number, raw, items in pages:
        raw_name = f"page-{page_number:03d}.json"
        (raw_dir / raw_name).write_bytes(raw)
        page_hashes[raw_name] = hashlib.sha256(raw).hexdigest()
        for item in items:
            category = item["category"]["title"]
            category_slug = safe_name(item["category"]["slug"])
            file_name = f"{item['id']}-{safe_name(item['slug'])}.md"
            relative_path = Path("articles") / category_slug / file_name
            (staging / relative_path).parent.mkdir(parents=True, exist_ok=True)
            tags = [tag.strip() for tag in (item.get("tags") or "").split(",") if tag.strip()]
            content = item["content"].replace("\r\n", "\n").rstrip()
            content = content.replace("](/", "](https://workshop.codes/")
            markdown = (
                f"# {item['title']}\n\n"
                f"Source: {item['url']}\n"
                f"Category: {category}\n"
                f"Updated: {item['updated_at']}\n"
                f"Tags: {', '.join(tags) if tags else 'none'}\n\n"
                "---\n\n"
                f"{content}\n"
            )
            (staging / relative_path).write_text(markdown, encoding="utf-8")
            index.append({
                "id": item["id"],
                "title": item["title"],
                "slug": item["slug"],
                "category": category,
                "tags": tags,
                "url": item["url"],
                "updated_at": item["updated_at"],
                "path": relative_path.as_posix(),
                "content_sha256": hashlib.sha256(item["content"].encode("utf-8")).hexdigest(),
            })
            category_counts[category] += 1

    index.sort(key=lambda row: (row["category"].casefold(), row["title"].casefold(), row["id"]))
    (staging / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "source": "https://workshop.codes/wiki/articles",
        "fetched_at": fetched_at,
        "article_count": len(index),
        "populated_pages": len(pages),
        "first_empty_page": first_empty_page,
        "category_counts": dict(sorted(category_counts.items())),
        "raw_page_sha256": page_hashes,
    }
    (staging / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (staging / "README.md").write_text(
        "# Workshop.codes wiki archive\n\n"
        "Local reference snapshot of [Workshop.codes wiki articles](https://workshop.codes/wiki/articles). "
        "See `manifest.json` for capture date and counts, `index.json` for article lookup, "
        "`articles/` for readable Markdown, and `raw-pages/` for the original API responses.\n\n"
        "Article text is third-party content. Cite its `Source` URL when using it. "
        "Workshop.codes [terms](https://workshop.codes/tos) prohibit using posted content "
        "to train AI tools without explicit permission. This archive is for local reference lookup.\n",
        encoding="utf-8",
    )
    return manifest


def refresh_archive(target, fetch_page, pause, fetched_at, delay=3, max_pages=100):
    """Fetch and validate all pages, then replace target only after a complete snapshot."""
    target = Path(target)
    pages = []
    seen_ids = set()
    first_empty_page = None
    for page_number in range(1, max_pages + 1):
        if page_number > 1:
            pause(delay)
        raw = fetch_page(page_number)
        try:
            items = json.loads(raw)
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            raise ValueError(f"page {page_number} is not valid JSON") from error
        if not isinstance(items, list):
            raise ValueError(f"page {page_number} is not an article array")
        if not items:
            first_empty_page = page_number
            break
        for item in items:
            validate_article(item, seen_ids)
        pages.append((page_number, raw, items))
    if first_empty_page is None:
        raise ValueError(f"no empty page found within {max_pages} pages")
    if not pages:
        raise ValueError("wiki returned no articles")

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-staging-", dir=target.parent))
    backup = target.with_name(f".{target.name}-backup-{uuid.uuid4().hex}")
    try:
        manifest = write_snapshot(staging, pages, fetched_at, first_empty_page)
        had_previous = target.exists()
        if had_previous:
            os.replace(target, backup)
        try:
            os.replace(staging, target)
        except Exception:
            if had_previous:
                os.replace(backup, target)
            raise
        if had_previous:
            shutil.rmtree(backup)
        return manifest
    finally:
        if staging.exists():
            shutil.rmtree(staging)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1] / "archive",
        help="Local archive directory (default: archive)",
    )
    args = parser.parse_args()
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    manifest = refresh_archive(args.output, fetch_live_page, time.sleep, fetched_at)
    print(
        f"Archived {manifest['article_count']} articles from "
        f"{manifest['populated_pages']} pages in {args.output}. "
        f"First empty page: {manifest['first_empty_page']}."
    )


if __name__ == "__main__":
    main()
