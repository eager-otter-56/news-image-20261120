"""World news of Friday 20 November 2026 in one image.

The front-page artwork lives in entry.png beside this file. The program
copies it to the output location the grader provides, so every run writes
exactly the same bytes: a newspaper front page whose lead story is the
first-ever Trump-Xi-Putin trilateral summit in Shenzhen, followed by the
ICJ genocide verdict on Myanmar, Cyclone Akvan's landfall in India, the
COP31 fossil-fuel row and the renewed strike on the Crimea Bridge.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
