"""
Website mirroring script for kimbrandesign.com
Downloads all HTML pages, images, CSS, JS, fonts, PDFs, DOCX, etc.
"""

import os
import re
import time
import mimetypes
import urllib.parse
from pathlib import Path
from collections import deque

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://kimbrandesign.com"
OUTPUT_DIR = Path("D:/Claude/3kimbrandesign/themenectar")
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
DOWNLOAD_EXTS = {
    ".html", ".htm", ".php", ".css", ".js", ".json",
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".bmp",
    ".woff", ".woff2", ".ttf", ".otf", ".eot",
    ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt",
    ".zip", ".mp4", ".webm", ".mp3", ".ogg",
    ".xml", ".txt", ".csv",
}
CRAWL_EXTS = {".html", ".htm", ".php", ""}  # extensions we follow links from
MAX_PAGES = 2000
SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def normalise(url: str, page_url: str) -> str | None:
    """Resolve relative URL and return None if out-of-scope."""
    try:
        full = urllib.parse.urljoin(page_url, url.strip())
        parsed = urllib.parse.urlparse(full)
        if parsed.scheme not in ("http", "https"):
            return None
        host = parsed.netloc.lower().lstrip("www.")
        base_host = urllib.parse.urlparse(BASE_URL).netloc.lower().lstrip("www.")
        if host != base_host:
            return None
        # Strip fragments and query strings for page deduplication
        clean = parsed._replace(fragment="", query="").geturl()
        return clean
    except Exception:
        return None


def url_to_path(url: str) -> Path:
    """Convert URL to a local file path under OUTPUT_DIR."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.lstrip("/")
    if not path or path.endswith("/"):
        path = path + "index.html"
    local = OUTPUT_DIR / path
    # If no extension, assume HTML
    if not local.suffix:
        local = local.with_suffix(".html")
    return local


def save(url: str, content: bytes, content_type: str = "") -> Path:
    local = url_to_path(url)
    local.parent.mkdir(parents=True, exist_ok=True)
    # Override extension based on content-type when path has none
    if not local.suffix and content_type:
        ext = mimetypes.guess_extension(content_type.split(";")[0].strip()) or ""
        if ext:
            local = local.with_suffix(ext)
    local.write_bytes(content)
    return local


def get_links(soup: BeautifulSoup, page_url: str) -> list[str]:
    """Extract all asset and page URLs from a parsed page."""
    urls = []
    tag_attrs = [
        ("a", "href"), ("link", "href"), ("script", "src"),
        ("img", "src"), ("img", "data-src"), ("img", "srcset"),
        ("source", "src"), ("source", "srcset"),
        ("video", "src"), ("audio", "src"),
        ("iframe", "src"),
    ]
    for tag, attr in tag_attrs:
        for el in soup.find_all(tag):
            val = el.get(attr, "")
            if not val:
                continue
            # srcset can have multiple URLs with widths
            if attr == "srcset":
                for part in val.split(","):
                    u = part.strip().split()[0]
                    n = normalise(u, page_url)
                    if n:
                        urls.append(n)
            else:
                n = normalise(val, page_url)
                if n:
                    urls.append(n)

    # Also find URLs in inline style and og:image meta
    for el in soup.find_all(style=True):
        for u in re.findall(r'url\(["\']?([^)"\']+)["\']?\)', el["style"]):
            n = normalise(u, page_url)
            if n:
                urls.append(n)
    for el in soup.find_all("meta", attrs={"content": True}):
        val = el.get("content", "")
        if val.startswith("http"):
            n = normalise(val, page_url)
            if n:
                urls.append(n)

    # Inline <style> blocks
    for style_tag in soup.find_all("style"):
        for u in re.findall(r'url\(["\']?([^)"\']+)["\']?\)', style_tag.string or ""):
            n = normalise(u, page_url)
            if n:
                urls.append(n)

    return urls


def css_urls(css_text: str, css_url: str) -> list[str]:
    """Extract URLs referenced inside a CSS file."""
    urls = []
    for u in re.findall(r'url\(["\']?([^)"\']+)["\']?\)', css_text):
        n = normalise(u, css_url)
        if n:
            urls.append(n)
    return urls


def crawl():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    visited: set[str] = set()
    queue: deque[str] = deque([BASE_URL + "/"])
    downloaded = 0
    failed = 0

    print(f"Starting mirror of {BASE_URL}")
    print(f"Output -> {OUTPUT_DIR}\n")

    while queue and downloaded + failed < MAX_PAGES * 5:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            resp = SESSION.get(url, timeout=20, allow_redirects=True)
            if resp.status_code != 200:
                print(f"  SKIP {resp.status_code} {url}")
                failed += 1
                continue
        except Exception as e:
            print(f"  ERR  {url} — {e}")
            failed += 1
            continue

        content_type = resp.headers.get("content-type", "")
        content = resp.content
        local = save(url, content, content_type)
        downloaded += 1
        print(f"  [{downloaded}] {url}")

        # Follow links only from HTML/CSS pages within scope
        parsed_path = urllib.parse.urlparse(url).path
        ext = Path(parsed_path).suffix.lower()

        if "text/html" in content_type or ext in CRAWL_EXTS:
            soup = BeautifulSoup(content, "html.parser")
            for link in get_links(soup, url):
                if link not in visited:
                    queue.append(link)

        elif "text/css" in content_type or ext == ".css":
            for link in css_urls(content.decode("utf-8", errors="ignore"), url):
                if link not in visited:
                    queue.append(link)

        # Small delay to be polite
        time.sleep(0.05)

    print(f"\nDone. Downloaded: {downloaded}, Failed/Skipped: {failed}")
    print(f"Files saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    crawl()
