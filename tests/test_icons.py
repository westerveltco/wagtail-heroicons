from __future__ import annotations

import itertools

import pytest
from django.template.loader import render_to_string
from django.template.utils import get_app_template_dirs
from wagtail import hooks

# Note: test_icon_rendering_in_admin was removed as it relied on
# wagtail.admin.views.home.icons which no longer exists in Wagtail 6+.
# Icon rendering is still tested by test_icon_rendering.


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
