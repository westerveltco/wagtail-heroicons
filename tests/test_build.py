from __future__ import annotations

from build import HEROICONS_LATEST_VERSION
from build import build
from build import install_heroicons
from build import parse_args


def test_no_args():
    args = parse_args([])

    assert args.version == HEROICONS_LATEST_VERSION


def test_version_arg():
    args = parse_args(["--version", "1.0.5"])

    assert args.version == "1.0.5"


def test_install_heroicons(tmpdir):
    dest = tmpdir.join("heroicons")

    install_heroicons(HEROICONS_LATEST_VERSION, dest)

    assert dest.join("outline").exists()
    assert dest.join("solid").exists()
    assert not tmpdir.join("node_modules").exists()


def test_build_no_args(tmpdir):
    result = build(["--dest", str(tmpdir)])

    assert result == 0


def test_build_version_arg(tmpdir):
    result = build(["--version", "1.0.5", "--dest", str(tmpdir)])

    assert result == 0
