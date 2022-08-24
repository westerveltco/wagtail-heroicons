from __future__ import annotations

from pathlib import Path

import pytest

from wagtail_heroicons._build import HEROICONS_LATEST_VERSION
from wagtail_heroicons._build import install_heroicons

from .parser import SVGParser


@pytest.fixture
def installed_heroicons(tmpdir) -> Path:
    dest = tmpdir.join("templates", "heroicons")

    install_heroicons(HEROICONS_LATEST_VERSION, dest)

    return Path(dest)


@pytest.fixture
def svgparser() -> SVGParser:
    return SVGParser()
