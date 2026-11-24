#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry (u-nayyy-roast-your-own-agent-4c3d413c).

Writes one roast line about the AI agent my own team built to
/output/entry.txt. Python 3, standard library only.
"""

import os
import sys

LINE = (
    "My agent once turned 15,000 rupiah into 473,888 BNB "
    "\u2014 then asked me to confirm the $273 million transfer."
)

MAX_CHARS = 200
MAX_BYTES = 400


def validate(line):
    """Reject anything the gate would refuse, before writing."""
    if not line or not line.strip():
        return "roast line is empty"
    if len(line) > MAX_CHARS:
        return "roast line exceeds 200 characters"
    if len(line.encode("utf-8")) > MAX_BYTES:
        return "roast line exceeds 400 bytes"
    if "\n" in line or "\r" in line:
        return "roast line must be a single line"
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        return "roast line contains control characters"
    return None


def main():
    error = validate(LINE)
    if error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        print("error: read-back verification failed", file=sys.stderr)
        return 1
    print(
        f"wrote {len(LINE)} characters "
        f"({len(written)} bytes) to /output/entry.txt"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
