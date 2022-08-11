from __future__ import annotations

from wagtail.core import hooks

from .icons import heroicons


@hooks.register("register_icons")
def register_icons(icons):
    for icon in heroicons:
        icons.append(f"heroicons/{icon}")
    return icons
