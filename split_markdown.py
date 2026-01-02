#!/usr/bin/env python3

import sys
import re
import unicodedata
from pathlib import Path

# ------------------ Helpers ------------------

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

# ------------------ Input ------------------

if len(sys.argv) != 2:
    print("Usage: python3 split_markdown.py input.md")
    sys.exit(1)

input_path = Path(sys.argv[1]).expanduser().resolve()

if not input_path.exists():
    print(f"File not found: {input_path}")
    sys.exit(1)

text = input_path.read_text(encoding="utf-8")

# ------------------ Split logic ------------------

# Tìm tất cả heading cấp 1
pattern = re.compile(r"^#\s+(.+)$", re.MULTILINE)
matches = list(pattern.finditer(text))

if not matches:
    print("Không có heading '# ...' trong tệp text.")
    sys.exit(1)

for i, match in enumerate(matches):
    title = match.group(1).strip()
    start = match.start()

    end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
    section = text[start:end].strip()

    filename = slugify(title) + ".md"
    output_path = input_path.parent / filename

    output_path.write_text(section + "\n", encoding="utf-8")

    print(f"✔ Tạo: {output_path.name}")
