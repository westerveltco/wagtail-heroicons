from __future__ import annotations

from pathlib import Path

from wagtail_heroicons._build import HEROICONS_LATEST_VERSION
from wagtail_heroicons._build import add_id_to_svg
from wagtail_heroicons._build import build
from wagtail_heroicons._build import generate_icon_registry
from wagtail_heroicons._build import install_heroicons
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


def test_generate_icon_registry(heroicon_installation_dir):
    icon_count = list(heroicon_installation_dir.rglob("*.svg"))

    icon_registry = generate_icon_registry(heroicon_installation_dir)

    assert len(icon_count) == len(icon_registry)


def test_add_id_to_svg(tmpdir, svgparser):
    file = tmpdir.join("dummy.svg")
    content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
        <path d="M0 0h24v24H0z" fill="none"/>
    </svg>
    """
    file.write(content)

    svg = add_id_to_svg(Path(file))

    svgparser.feed(svg.read_text())

    assert svgparser.found_id
    assert svgparser.id.startswith("icon-heroicons-dummy")


def test_write_icon_registry(heroicon_installation_dir):
    icon_registry = generate_icon_registry(heroicon_installation_dir)

    write_icon_registry(icon_registry, heroicon_installation_dir / "icon_registry.py")

    assert Path(heroicon_installation_dir / "icon_registry.py").exists()


def test_build_no_args(tmpdir):
    result = build(["--dest", str(tmpdir)])

    assert result == 0


def test_build_version_arg(tmpdir):
    result = build(["--version", "1.0.5", "--dest", str(tmpdir)])

    assert result == 0
