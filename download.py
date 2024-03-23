#!/usr/bin/env python
from __future__ import annotations

import argparse
import shutil
from collections.abc import Sequence
from pathlib import Path
from tempfile import TemporaryDirectory

import httpx
from bs4 import BeautifulSoup
from bs4 import Comment

HEROICONS_LATEST_VERSION = "1.0.6"

DEST_DIR = (
    Path(__file__).parent
    / "src"
    / "wagtail_heroicons"
    / "templates"
    / "wagtail_heroicons"
)


def main(argv: Sequence[str] | None = None) -> int:
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
    args = parser.parse_args(argv)

    version = args.version
    dest = args.dest

    response = httpx.get(
        f"https://github.com/tailwindlabs/heroicons/archive/v{version}.zip",
        follow_redirects=True,
    ).raise_for_status()

    with TemporaryDirectory() as tmpdir:
        with open(Path(tmpdir) / "heroicons.zip", "wb") as f:
            f.write(response.content)

        shutil.unpack_archive(Path(tmpdir) / "heroicons.zip", tmpdir)

        for icon_type_path in (
            Path(tmpdir) / f"heroicons-{version}" / "optimized"
        ).iterdir():
            icon_type_folder = Path(dest) / icon_type_path.name

            shutil.rmtree(icon_type_folder, ignore_errors=True)
            shutil.copytree(icon_type_path, icon_type_folder)

    for icon_path in dest.rglob("*.svg"):
        with open(icon_path) as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        for icon in soup.find_all("svg"):
            icon_name = icon_path.stem
            icon_type = icon_path.parent.name

            icon.attrs["id"] = f"icon-heroicons-{icon_name}-{icon_type}"

            icon.insert(0, Comment(" MIT License https://mit-license.org/ "))
            icon.insert(1, Comment(" Copyright (c) 2020 Refactoring UI Inc. "))

        with open(icon_path, "wb") as f:
            f.write(soup.prettify("utf-8"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
