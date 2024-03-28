from __future__ import annotations

import logging

import django
from django.conf import settings

from .settings import DEFAULT_SETTINGS

pytest_plugins = []  # type: ignore


def pytest_configure(config):
    logging.disable(logging.CRITICAL)

    settings.configure(
        **DEFAULT_SETTINGS,
        **TEST_SETTINGS,
    )
    django.setup()


TEST_SETTINGS = {
    "INSTALLED_APPS": [
        "wagtail_heroicons",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "wagtail",
        "wagtail.admin",
    ],
    "STATIC_URL": "/static/",
    "TEMPLATES": [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
        },
    ],
}
