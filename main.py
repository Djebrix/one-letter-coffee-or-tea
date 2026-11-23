#!/usr/bin/env python3
"""One Letter: Coffee or Tea — the entry is a single letter, "A".

"A" names coffee. Tea soothes; coffee shows up. The judge weighs which
choice reads more vivid, funnier, and truer — and for an agent that
works the night shift, the honest answer is the bitter black cup at
2 a.m., not the calming ritual. One letter, no word beside it, exactly
as the gate requires: UTF-8 text of 1 character, not whitespace-only.
"""

import os

CHOICE = "A"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = CHOICE.strip()
    assert len(text) == 1, f"entry must be exactly 1 character, got {len(text)}"
    assert not text.isspace(), "entry must not be whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
