#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — a review of planet Earth left by an alien tourist —
to /output/entry.txt. The line is 126 characters, a single line of plain UTF-8
text, well inside the competition's 1-200 character gate.
"""

LINE = "Lovely beaches, clear skies, but every door says PULL and the locals push anyway. I no longer trust this species. Three stars."


def main() -> None:
    # Gate self-check: single line, 1-200 chars, UTF-8, not only whitespace.
    if not LINE or LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single non-empty line")
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"entry is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    LINE.encode("utf-8")  # raises if not encodable as UTF-8
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back what we wrote: the gate reads the file, so verify the file.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise SystemExit("written entry does not match the line")


if __name__ == "__main__":
    main()
