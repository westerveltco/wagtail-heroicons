from __future__ import annotations

from wagtail_heroicons.icons import Heroicon


def test_get_icons(installed_heroicons):
    icons = Heroicon.get_icons()

    assert len(icons) != 0


def test_add_id(installed_heroicons, svgparser):
    icon = Heroicon.get_icons()[0]

    icon._add_id()

    svgparser.feed(icon.path.read_text())

    assert svgparser.found_id
    assert svgparser.id.startswith("icon-heroicons-")
