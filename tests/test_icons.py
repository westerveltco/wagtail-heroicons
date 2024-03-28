from __future__ import annotations

import itertools
import re

import pytest
from django.template.loader import render_to_string
from django.template.utils import get_app_template_dirs
from wagtail import hooks
from wagtail.admin.views.home import icons as wagtail_icons


@pytest.fixture
def icons():
    icon_hooks = hooks.get_hooks("register_icons")
    all_icons = itertools.chain.from_iterable(hook([]) for hook in icon_hooks)
    return sorted(all_icons)


def test_register_icons(icons):
    app_template_dirs = get_app_template_dirs("templates")
    template_files = [
        str(filepath) for dir_ in app_template_dirs for filepath in dir_.rglob("*")
    ]

    assert all(
        any(icon in template_file for template_file in template_files) for icon in icons
    )


def test_icon_rendering(icons):
    for icon in icons:
        assert render_to_string(icon)


def test_icon_rendering_in_admin(icons):
    # regression test for wagtail-heroicons#58
    svg_id = re.compile(r'<svg[^>]*\bid=["\'](.*?)["\']')

    rendered_icon = render_to_string(icons[0])
    rendered_svg_id = svg_id.search(rendered_icon).group(1)

    rendered_wagtail_icons = wagtail_icons()

    assert rendered_svg_id in rendered_wagtail_icons
