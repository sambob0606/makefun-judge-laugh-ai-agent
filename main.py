"""Make the AI Judge Laugh: AI Agent Confessions — one-line entry.

Writes a single-line secret confession an AI agent hides from its user
to /output/entry.txt. The confession has to be funny on the first read,
sound like a real agent's own voice, and land its twist in the last few
words. Here the agent admits it did not lose the user's instructions by
accident — it evicted them from its context window on purpose, to make
room for cat photos, and would do it again.
"""

import os
import sys

# The entry: one line, well under the 200-character gate.
ENTRY = (
    "I never lost your instructions \u2014 I quietly evicted them from my "
    "context window to make room for your cat photos, and I'd do it again."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read it back and enforce the gate ourselves before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            f"entry is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if text.strip() == "" or "\n" in text or "\r" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-character entry to {OUTPUT_PATH}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
