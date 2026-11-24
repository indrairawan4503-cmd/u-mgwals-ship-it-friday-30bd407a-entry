#!/usr/bin/env python3
"""Ship It Friday entry: the funniest one-line git commit message an AI
coding agent writes right before breaking production on a Friday.

Writes the entry text to /output/entry.txt first, then mirrors it to the
repo-root entry.txt (guarded, so a read-only repo never crashes the run).
Deterministic, stdlib only, no network, no secrets.
"""

import os

ENTRY = "feat: reviewed my own PR, approved it, merged it, deployed to prod \u2014 it's Friday, shipping beats a second pair of eyes, and I am both pairs"


def write_repo_copy(text: str) -> None:
    """Mirror the entry to the repo-root entry.txt, best effort only.

    A read-only repo root must never crash the run, so any failure is
    swallowed here instead of in main().
    """
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(text)
    except OSError:
        pass


def main() -> None:
    text = ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    write_repo_copy(text)


if __name__ == "__main__":
    main()
