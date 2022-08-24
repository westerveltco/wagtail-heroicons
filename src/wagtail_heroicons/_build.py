#!/usr/bin/env python
from __future__ import annotations

import argparse
import shutil
from collections.abc import Sequence
from pathlib import Path

from nodejs import npm

from wagtail_heroicons.icons import Heroicon

HEROICONS_LATEST_VERSION = "2.0.0"

NODE_SRC_DIR = Path(__file__).parent.parent.parent / "node_modules" / "heroicons"
DEST_DIR = Path(__file__).parent / "templates" / "heroicons"


def build(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    install_heroicons(args.version, args.dest)

    for icon in Heroicon.get_icons():
        icon._add_id()

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


def install_heroicons(version: str, dest: Path) -> None:
    npm.run(["install", f"heroicons@{version}", "--silent", "--no-save"])

    icon_types = [
        {
            "size": "20",
            "dir": "solid",
            "name": "mini",
        },
        {
            "size": "24",
            "dir": "solid",
            "name": "solid",
        },
        {
            "size": "24",
            "dir": "outline",
            "name": "outline",
        },
    ]

    for icon_type in icon_types:
        shutil.rmtree(dest / icon_type["name"], ignore_errors=True)
        shutil.copytree(
            NODE_SRC_DIR / icon_type["size"] / icon_type["dir"],
            dest / icon_type["name"],
        )

    shutil.rmtree("node_modules")


if __name__ == "__main__":
    raise SystemExit(build())
