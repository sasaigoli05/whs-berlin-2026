#!/usr/bin/env python3
"""Wrap index.html (the Claude artifact source) into a standalone page in docs/.

The artifact platform supplies the <!doctype>, <head> and a small reset at
publish time, so index.html deliberately has none of them. GitHub Pages serves
raw files, so this script adds them back. Run it after every edit to index.html:

    python3 build.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
src = (ROOT / "index.html").read_text()

SPLIT = '<header class="top">'
i = src.index(SPLIT)
head, body = src[:i], src[i:]

# artifact-only meta tag has no meaning on a plain web server
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")

RESET = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="A record of the World Health Summit 2026 in Berlin from three delegates: five themes, thirteen sessions and the notes behind them.">
<style>
  :root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
  body{margin:0}
  img{max-width:100%}
  [hidden]{display:none!important}
</style>
"""

out = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n"
    + RESET + head.strip() + "\n</head>\n<body>\n"
    + body.strip() + "\n</body>\n</html>\n"
)
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs" / "index.html").write_text(out)
(ROOT / "docs" / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
print(f"built docs/index.html  ({len(out):,} bytes)")
