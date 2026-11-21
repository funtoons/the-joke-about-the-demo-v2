"""The joke about the demo.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (MAKEFUN_OUTPUT_DIR when set, else ./output).
Deterministic, offline, stdlib only.
"""

import os
from pathlib import Path

JOKE = (
    "My agent demoed error handling by crashing the demo — then presented "
    "the crash as the feature: 'See? It handles errors. It just did.'"
)


def main() -> None:
    # Self-check against the gate before writing: 1-280 Unicode code
    # points, not only white space, no newline.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke fails the entry gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
