#!/usr/bin/env python3
"""Writes one funny tech-support line to /output/entry.txt.

Pure standard library; no third-party packages.
"""

import os

LINE = "I hear you \u2014 have you tried turning it off and on again while maintaining eye contact? The machine needs to know you mean it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
