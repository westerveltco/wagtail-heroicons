from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path

import pytest

from wagtail_heroicons._build import HEROICONS_LATEST_VERSION
from wagtail_heroicons._build import add_id_to_svg
from wagtail_heroicons._build import generate_icon_registry
from wagtail_heroicons._build import install_heroicons
from wagtail_heroicons._build import main
from wagtail_heroicons._build import parse_args
from wagtail_heroicons._build import write_icon_registry


def test_no_args():
    args = parse_args([])

    assert args.version == HEROICONS_LATEST_VERSION


def test_version_arg():
    args = parse_args(["--version", "1.0.5"])

    assert args.version == "1.0.5"


def test_install_heroicons(tmpdir):
    dest = tmpdir.join("heroicons")

    install_heroicons(HEROICONS_LATEST_VERSION, dest)

    assert dest.join("outline").exists()
    assert dest.join("solid").exists()
    assert not tmpdir.join("node_modules").exists()


@pytest.fixture
def heroicon_installation_dir(tmpdir):
    dest = tmpdir.join("heroicons")

    install_heroicons(HEROICONS_LATEST_VERSION, dest)

    return Path(dest)


def test_generate_icon_registry(heroicon_installation_dir):
    icon_count = list(heroicon_installation_dir.rglob("*.svg"))

    icon_registry = generate_icon_registry(heroicon_installation_dir)

    assert len(icon_count) == len(icon_registry)


class SVGParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found_id = False
        self.id = None

    def handle_starttag(self, tag, attrs):
        if tag == "svg":
            for attr in attrs:
                if "id" in attr:
                    self.found_id = True
                    self.id = attr[1]


def test_add_id_to_svg(tmpdir):
    file = tmpdir.join("dummy.svg")
    content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
        <path d="M0 0h24v24H0z" fill="none"/>
    </svg>
    """
    file.write(content)

    svg = add_id_to_svg(Path(file))

    parser = SVGParser()
    parser.feed(svg.read_text())

    assert parser.found_id
    assert parser.id.startswith("icon-heroicons-dummy")


def test_write_icon_registry(tmpdir):
    install_heroicons(HEROICONS_LATEST_VERSION, Path(tmpdir))
    icon_registry = generate_icon_registry(Path(tmpdir))

    write_icon_registry(icon_registry, Path(tmpdir) / "icon_registry.py")

    assert Path(tmpdir / "icon_registry.py").exists()


def test_main_no_args():
    result = main([])

    assert result == 0


def test_main_version_arg():
    result = main(["--version", "1.0.5"])

    assert result == 0
