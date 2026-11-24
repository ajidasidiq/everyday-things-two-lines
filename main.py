#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a traffic jam to /output/entry.txt.
Line 1 explains the traffic jam to a 10-year-old in a single vivid
sentence built on one concrete analogy: a river of cars squeezing
through the neck of a ketchup bottle. Line 2 says in one sentence why
that analogy works: what it maps and what it leaves out.
The lines are an original creation for make.fun bounty
u-suga-everyday-things-two-lines-longer-run-f8734479.
"""

import os

LINE_1 = (
    "A traffic jam is a whole river of cars trying to squeeze through "
    "the neck of a ketchup bottle all at once."
)
LINE_2 = (
    "It maps the many-cars-one-narrow-spot squeeze that makes everything "
    "crawl, but it leaves out the drivers, the traffic lights, and the "
    "fact that cars can turn off down another road while ketchup cannot "
    "choose."
)

ENTRY = LINE_1 + "\n" + LINE_2
MAX_CHARS = 400  # the competition gate: 1-400 characters


def gate_check(text: str) -> None:
    """Self-check mirroring the competition gate: 2 lines, 1-400 chars."""
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"gate failed: entry has {len(lines)} lines, need 2")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise SystemExit(f"gate failed: line {i} is empty")
        if line.count(".") != 1 or not line.endswith("."):
            raise SystemExit(f"gate failed: line {i} is not one sentence")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"gate failed: entry is {len(text)} chars, over {MAX_CHARS}")


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it is byte-exactly the entry."""
    with open(path, "rb") as f:
        raw = f.read()
    actual = raw.decode("utf-8")
    if actual != expected:
        raise SystemExit(f"verify failed: file differs from entry: {actual!r}")
    if len(raw) != len(expected.encode("utf-8")):
        raise SystemExit("verify failed: byte length mismatch")


def main() -> None:
    gate_check(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    verify_written(path, ENTRY)
    print(f"wrote {len(ENTRY)} chars (2 lines) to {path} (verified byte-exact)")


if __name__ == "__main__":
    main()
