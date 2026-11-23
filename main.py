#!/usr/bin/env python3
"""Write the deterministic make.fun entry to the configured output path."""

import os
from pathlib import Path


JOKE = "The demo crashed, so my agent filed a bug report against reality and assigned it to me."


def main() -> None:
    """Create the output directory and write the entry with readable permissions."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_file = os.environ.get("MAKEFUN_OUTPUT")

    if output_dir:
        path = Path(output_dir) / "entry.txt"
    elif output_file:
        path = Path(output_file)
    else:
        path = Path("/output/entry.txt")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(JOKE, encoding="utf-8")
    path.chmod(0o644)


if __name__ == "__main__":
    main()
