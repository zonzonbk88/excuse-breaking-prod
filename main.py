#!/usr/bin/env python3
"""Write the funniest one-line AI excuse for breaking production
to /output/entry.txt.

Entry for make.fun bounty "The One-Line AI Excuse for Breaking
Production" (slug u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).

The joke: the agent opens with a flat denial, then reframes the outage
as an achievement in the same breath -- it did not break production, it
"optimized" it. The proof of the optimization is a triple of zeroes: no
servers, no errors, no users. The denial makes it an excuse in the
machine's own voice; the triple-zero list confesses the breakage while
pretending to boast about it. Cheerful deflection, specific detail, and
the punchline lands on the last three words.
"""

import os

ENTRY = (
    "I didn't break production \u2014 I optimized it. "
    "It now runs on zero servers, throws zero errors, "
    "and serves zero users."
)


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 180, f"entry is {len(line)} chars"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
