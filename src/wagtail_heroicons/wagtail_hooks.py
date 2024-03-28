from __future__ import annotations

from pathlib import Path

from wagtail import hooks


@hooks.register("register_icons")
def register_icons(icons):
    template_dir = Path(__file__).parent / "templates" / "wagtail_heroicons"
    heroicons = [
        f"wagtail_heroicons/{file.parent.name}/{file.name}"
        for file in template_dir.rglob("*.svg")
    ]
    return icons + heroicons
