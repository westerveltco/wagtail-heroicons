from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path

import pytest

from wagtail_heroicons._build import HEROICONS_LATEST_VERSION
from wagtail_heroicons._build import install_heroicons


@pytest.fixture
def heroicon_installation_dir(tmpdir):
    dest = tmpdir.join("heroicons")

    install_heroicons(HEROICONS_LATEST_VERSION, dest)

    return Path(dest)


@pytest.fixture
def svgparser():
    class SVGParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.found_id = False
            self.id = None

        def handle_starttag(self, tag, attrs):
            if tag == "svg":
                for attr in attrs:
                    if "id" in attr:
                        self.found_id = True
                        self.id = attr[1]

    return SVGParser()
