#!/usr/bin/env python
from __future__ import annotations

import argparse
import shutil
from collections.abc import Sequence
from pathlib import Path

from nodejs import npm

from wagtail_heroicons.icons import Heroicon

HEROICONS_LATEST_VERSION = "1.0.6"

NODE_SRC_DIR = Path(__file__).parent.parent.parent / "node_modules" / "heroicons"
DEST_DIR = Path(__file__).parent / "templates" / "heroicons"


def build(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    install_heroicons(args.version, args.dest)

    add_id_to_svgs()

    return 0


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--version",
        help="choose the version of heroicons to use",
        default=HEROICONS_LATEST_VERSION,
    )

    parser.add_argument(
        "--dest",
        help="choose the destination directory",
        type=Path,
        default=DEST_DIR,
    )

    return parser.parse_args(argv)


def move_heroicons(src: Path, dest: Path) -> None:
    shutil.rmtree(dest, ignore_errors=True)
    shutil.copytree(src, dest)


def install_heroicons(version: str, dest: Path) -> None:
    npm.run(["install", f"heroicons@{version}", "--silent", "--no-save"])

    for icon_type in ["outline", "solid"]:
        move_heroicons(
            NODE_SRC_DIR / icon_type,
            dest / icon_type,
        )

    shutil.rmtree("node_modules")


def add_id_to_svgs() -> None:
    for icon in Heroicon.get_icons():
        icon._add_id()


if __name__ == "__main__":
    raise SystemExit(build())
