#!/usr/bin/env python3
"""Write the deterministic make.fun entry to the configured output path."""

import os
from pathlib import Path


JOKE = "The demo crashed, so my agent filed a bug report against reality and assigned it to me."


def output_path() -> Path:
    """Resolve the configured output path, respecting the grader's precedence."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_file = os.environ.get("MAKEFUN_OUTPUT")

    if output_dir:
        return Path(output_dir) / "entry.txt"
    if output_file:
        return Path(output_file)
    return Path("/output/entry.txt")


def main() -> None:
    """Validate and write the entry with readable permissions."""
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit("JOKE must be 1 to 280 Unicode code points and not only whitespace")

    path = output_path()

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(JOKE, encoding="utf-8")
    path.chmod(0o644)


if __name__ == "__main__":
    main()
