from __future__ import annotations

from wagtail_heroicons.icons import Heroicon


def test_get_icons():
    icons = Heroicon.get_icons()

    assert len(icons) != 0
