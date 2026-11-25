#!/usr/bin/env python3
"""Writes one funny tech-support line to /output/entry.txt.

Pure standard library; no third-party packages. The line is validated
against the competition gate before it is written: UTF-8 text, 1-199
characters, a single line, and not only whitespace.
"""

import os

LINE = "I hear you \u2014 have you tried turning it off and on again while maintaining eye contact? The machine needs to know you mean it."

def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
