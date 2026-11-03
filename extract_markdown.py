#!/usr/bin/env python
#*-----------------------------------------------------------------------*
#|                                                                       |
#|  Copyright (c) 2026 generated mostly with chatgpt                     |
#|                                                                       |
#|              Author Thierry Zamofing (th.zamofing@gmail.com)          |
#*-----------------------------------------------------------------------*
'''
converts text only of html pages to mardown
'''

from pathlib import Path
from bs4 import BeautifulSoup
import re

source = Path("_orig/www.praxis-weiterkommen.com/")
target = Path("_orig/md")

target.mkdir(parents=True, exist_ok=True)

for html_file in source.rglob("*"):
  if not html_file.is_file() or html_file.suffix.lower() not in (".html", ".htm"):
    continue
  soup = BeautifulSoup(
    html_file.read_text(encoding="utf-8", errors="replace"),
    "html.parser"
  )

  for element in soup([
    "script", "style", "noscript",
    "header", "footer", "nav"
  ]):
    element.decompose()

  main = soup.find("main") or soup.find("article") or soup.body or soup

  title = soup.title.get_text(strip=True) if soup.title else html_file.stem

  # Preserve headings and paragraph separation
  for tag in main.find_all(["br"]):
    tag.replace_with("\n")

  text = main.get_text(separator="\n\n", strip=True)
  text = re.sub(r"\n{3,}", "\n\n", text)

  # Preserve relative directory structure
  relative = html_file.relative_to(source)
  output = target / relative.parent / f"{relative.stem}.md"
  output.parent.mkdir(parents=True, exist_ok=True)

  markdown = f'---\ntitle: "{title}"\n---\n\n{text}\n'

  output.write_text(markdown, encoding="utf-8")

  print(f"Created: {output}")