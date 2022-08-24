from __future__ import annotations

from wagtail.core import hooks

from .icons import Heroicon


@hooks.register("register_icons")
def register_icons(icons):
    for icon in Heroicon.get_icons():
        icons.append(icon.path)
    return icons
