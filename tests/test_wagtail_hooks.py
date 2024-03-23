from __future__ import annotations

import itertools

from django.template.utils import get_app_template_dirs
from wagtail import hooks


def test_register_icons():
    icon_hooks = hooks.get_hooks("register_icons")
    print("icon_hooks", icon_hooks)
    for hook in icon_hooks:
        print(hook.__module__)
    all_icons = sorted(itertools.chain.from_iterable(hook([]) for hook in icon_hooks))

    app_template_dirs = get_app_template_dirs("templates")
    template_files = [
        str(filepath) for dir_ in app_template_dirs for filepath in dir_.rglob("*")
    ]

    print("all_icons")
    print(*all_icons, sep="\n")
    print("template_files")
    print(*template_files, sep="\n")

    assert all(
        any(template_file.endswith(f"{icon}.svg") for template_file in template_files)
        for icon in all_icons
    )
