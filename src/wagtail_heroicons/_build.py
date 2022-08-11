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

    install_heroicons(args.version, DEST_DIR)

    icon_registry = generate_icon_registry()

    write_icon_registry(icon_registry)

    return 0


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--version",
        help="choose the version of heroicons to use",
        default=HEROICONS_LATEST_VERSION,
    )

    return parser.parse_args(argv)


def install_heroicons(version: str, dest: Path) -> None:
    npm.run(["install", f"heroicons@{version}", "--silent", "--no-save"])

    for icon_type in ["outline", "solid"]:
        shutil.copytree(
            f"{NODE_SRC_DIR}/{icon_type}",
            f"{dest}/{icon_type}",
            dirs_exist_ok=True,
        )

    shutil.rmtree("node_modules")


def generate_icon_registry() -> list[str]:
    icon_registry = []

    for child in DEST_DIR.rglob("*.svg"):
        with child.open("r") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        for icon in soup.find_all("svg"):
            # Wagtail uses the id attribute to identify icons. The name used in Wagtail
            # is the id attribute of the <svg> tag, minus the "icon-" prefix.
            icon.attrs["id"] = f"icon-heroicons-{child.stem}-{child.parent.name}"

            icon_registry.append(f"{child.parent.name}/{child.stem}.svg")

        with child.open("wb") as f:
            f.write(soup.prettify("utf-8"))

    return sorted(icon_registry)


def write_icon_registry(icon_registry: list[str]) -> None:
    list_str = "".join(f'\n    "{icon_name}", ' for icon_name in icon_registry)

    output = f"""
from __future__ import annotations

heroicons = [{list_str}]
"""

    with Path("src/wagtail_heroicons/icons.py").open("w") as f:
        f.write(output)


if __name__ == "__main__":
    raise SystemExit(main())
