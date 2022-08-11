#!/usr/bin/env python
from __future__ import annotations

import argparse
import shutil
from collections.abc import Sequence
from pathlib import Path

from bs4 import BeautifulSoup
from nodejs import npm

HEROICONS_LATEST_VERSION = "1.0.6"
NODE_SRC_DIR = Path("node_modules/heroicons")
DEST_DIR = Path("src/wagtail_heroicons/templates/heroicons")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    install_heroicons(args.version, args.dest)

    icon_registry = generate_icon_registry(args.dest)

    write_icon_registry(icon_registry, Path("src/wagtail_heroicons/icons.py"))

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

    for icon_type in ["outline", "solid"]:
        shutil.rmtree(f"{dest}/{icon_type}", ignore_errors=True)
        shutil.copytree(
            f"{NODE_SRC_DIR}/{icon_type}",
            f"{dest}/{icon_type}",
        )

    shutil.rmtree("node_modules")


def generate_icon_registry(dest: Path) -> list[str]:
    icon_registry = []

    for child in dest.rglob("*.svg"):
        svg = add_id_to_svg(child)
        icon_registry.append(f"{svg.parent.name}/{svg.stem}.svg")

    return sorted(icon_registry)


def add_id_to_svg(svg: Path) -> Path:
    with svg.open("r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for icon in soup.find_all("svg"):
        # Wagtail uses the id attribute to identify icons. The name used in Wagtail
        # is the id attribute of the <svg> tag, minus the "icon-" prefix.
        icon.attrs["id"] = f"icon-heroicons-{svg.stem}-{svg.parent.name}"

    with svg.open("wb") as f:
        f.write(soup.prettify("utf-8"))

    return svg


def write_icon_registry(icon_registry: list[str], path: Path) -> None:
    list_str = "".join(f'\n    "{icon_name}",' for icon_name in icon_registry)

    output = f"""from __future__ import annotations

heroicons = [{list_str}\n]
"""

    with path.open("w") as f:
        f.write(output)


if __name__ == "__main__":
    raise SystemExit(main())
