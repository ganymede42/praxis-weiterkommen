#!/usr/bin/env python
#*-----------------------------------------------------------------------*
#|                                                                       |
#|  Copyright (c) 2026 generated mostly with chatgpt                     |
#|                                                                       |
#|              Author Thierry Zamofing (th.zamofing@gmail.com)          |
#*-----------------------------------------------------------------------*
'''
extracts text only of html pages
'''


from pathlib import Path
from bs4 import BeautifulSoup
import re

source = Path("_orig/www.praxis-weiterkommen.com/")
target = Path("_orig/txt")

target.mkdir(exist_ok=True)

for html_file in source.rglob("*"):
  if not html_file.is_file() or html_file.suffix.lower() not in (".html", ".htm"):
    continue

  content = html_file.read_text(
    encoding="utf-8",
    errors="replace"
  )

  soup = BeautifulSoup(content, "html.parser")

  # Remove elements that are not page content
  for element in soup([
    "script", "style", "noscript",
    "header", "footer", "nav"
  ]):
    element.decompose()

  # Prefer main content if available
  main = soup.find("main") or soup.find("article") or soup.body or soup

  # Extract text
  text = main.get_text(separator="\n", strip=True)

  # Remove excessive empty lines
  text = re.sub(r"\n{3,}", "\n\n", text)

  # Preserve relative directory structure
  relative = html_file.relative_to(source)
  output = target / relative.parent / f"{relative.stem}.txt"
  output.parent.mkdir(parents=True, exist_ok=True)

  output.write_text(text, encoding="utf-8")

  print(f"Extracted: {html_file} -> {output}")