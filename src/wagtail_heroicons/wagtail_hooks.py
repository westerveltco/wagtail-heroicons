from __future__ import annotations

from wagtail.core import hooks

from .icons import heroicons


@hooks.register("register_icons")
def register_icons(_icons):
    for icon in heroicons:
        _icons.append(f"heroicons/{icon}")
    return _icons
