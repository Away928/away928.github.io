#!/usr/bin/env python3
"""Offline check for the privacy-scoped portfolio landing page."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "style.css").read_text(encoding="utf-8")

class Inspect(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.img = []
        self.links = []
        self.scripts = 0
        self.headings = []
        self.main = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img":
            self.img.append(a)
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag == "script":
            self.scripts += 1
        if tag in {"h1", "h2", "h3"}:
            self.headings.append(tag)
        if tag == "main":
            self.main += 1

p = Inspect()
p.feed(HTML)
repos = [
    "https://github.com/Away928/ai-research-agent",
    "https://github.com/Away928/knowledge-system-public-core",
    "https://github.com/Away928/ai-infrastructure-public-core",
]
assert p.main == 1
assert p.headings.count("h1") == 1
assert p.headings.count("h3") == 3
assert p.scripts == 0
assert len(p.img) == 1 and p.img[0]["alt"] and (ROOT / p.img[0]["src"]).is_file()
assert all(p.links.count(u) == 1 for u in repos)
assert p.links.count("https://away928.github.io/ai-research-agent/") == 1
assert len(p.links) == 4
assert (ROOT / "avatar.png").stat().st_size > 1000
assert (ROOT / "avatar.png").read_bytes().startswith(b"\x89PNG")
assert re.search(r'<meta name="viewport"', HTML)
assert "@media (max-width: 480px)" in CSS
assert "@media (prefers-reduced-motion: reduce)" in CSS
assert "font-family" in CSS
assert not re.search(r'(contributions|followers|following|activity feed|cookie|analytics|track(?:er|ing))', HTML, flags=re.I)
assert not re.search(r'/Users/|gmail\.com|qq\.com|sk-ant-|github_pat_', HTML + CSS, flags=re.I)
assert not re.search(r'<(?:iframe|form|input|button)', HTML, flags=re.I)
print("PASS: focused profile + 3 repo cards, 1 synthetic demo link; local image and styles; responsive; no tracking")
