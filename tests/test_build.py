from __future__ import annotations

from wagtail_heroicons._build import HEROICONS_LATEST_VERSION
from wagtail_heroicons._build import parse_args


def test_no_args():
    args = parse_args([])

    assert args.version == HEROICONS_LATEST_VERSION

def test_version_arg():
    args = parse_args(["--version", "1.0.5"])

    assert args.version == "1.0.5"
