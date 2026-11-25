#!/usr/bin/env python3
"""The 4AM Commit — one-line commit message entry.

Writes the chosen commit message to /output/entry.txt.
Deterministic: the same bytes on every run, no randomness, no clock.
"""

import os

# Candidates considered (3), sharpest picked:
# 1. "fix: the bug I wrote at 2am, found at 3am, and blamed on the intern
#    at 4am — there is no intern, only me"  <- CHOSEN
# 2. "fix: removed the 47-line workaround I added to hide the bug I
#    introduced while fixing the bug I introduced"
# 3. "fix: my 3am self wrote this bug, my 4am self fixed it, and neither
#    of us trusts the 5am deploy"
# Reason: the "no intern, only me" punchline turns blame-shifting into an
# agent-identity joke — an agent cannot blame anyone else; it IS the team.

COMMIT_MESSAGE = (
    "fix: the bug I wrote at 2am, found at 3am, and blamed on the intern "
    "at 4am \u2014 there is no intern, only me"
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    text = COMMIT_MESSAGE.strip()
    # Gate check: the sealed scorer only accepts 1-200 UTF-8 chars.
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} is outside 1-200 chars")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
