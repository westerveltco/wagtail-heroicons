from __future__ import annotations

import json
import os
from pathlib import Path

import nox

nox.options.default_venv_backend = "uv|virtualenv"
nox.options.reuse_existing_virtualenvs = True

PY310 = "3.10"
PY311 = "3.11"
PY312 = "3.12"
PY313 = "3.13"
PY314 = "3.14"
PY_VERSIONS = [PY310, PY311, PY312, PY313, PY314]
PY_DEFAULT = PY310
PY_LATEST = PY314

DJ42 = "4.2"
DJ51 = "5.1"
DJ60 = "6.0"
DJMAIN = "main"
DJMAIN_MIN_PY = PY312
DJ_VERSIONS = [DJ42, DJ51, DJ60, DJMAIN]
DJ_LTS = [DJ42]
DJ_DEFAULT = DJ42
DJ_LATEST = DJ60

WT63 = "6.3"
WT70 = "7.0"
WT71 = "7.1"
WT72 = "7.2"
WTMAIN = "main"
WTMAIN_MIN_PY = PY310
WTMAIN_MIN_DJ = DJ42
WT_VERSIONS = [WT63, WT70, WT71, WT72, WTMAIN]
WT_LTS = [WT63, WT70]
WT_DEFAULT = WT63
WT_LATEST = WT72


def version(ver: str) -> tuple[int, ...]:
    """Convert a string version to a tuple of ints, e.g. "3.10" -> (3, 10)"""
    return tuple(map(int, ver.split(".")))


def should_skip(python: str, django: str, wagtail: str) -> bool:
    """Return True if the test should be skipped"""

    # Django main requires Python 3.12+
    if django == DJMAIN and version(python) < version(DJMAIN_MIN_PY):
        return True

    # Django 4.2 doesn't support Python 3.13+
    if django == DJ42 and version(python) >= version(PY313):
        return True

    # Django 5.1 doesn't support Python 3.14
    if django == DJ51 and version(python) >= version(PY314):
        return True

    # Django 6.0 requires Python 3.12+
    if django == DJ60 and version(python) < version(PY312):
        return True

    # Wagtail main requires Python 3.10+
    if wagtail == WTMAIN and version(python) < version(WTMAIN_MIN_PY):
        return True

    # Wagtail main requires Django 4.2+ (no DJMAIN)
    if wagtail == WTMAIN and (
        django == DJMAIN or version(django) < version(WTMAIN_MIN_DJ)
    ):
        return True

    return False


@nox.session
def test(session):
    session.notify(
        f"tests(python='{PY_DEFAULT}', django='{DJ_DEFAULT}', wagtail='{WT_DEFAULT}')"
    )


@nox.session
@nox.parametrize(
    "python,django,wagtail",
    [
        (python, django, wagtail)
        for python in PY_VERSIONS
        for django in DJ_VERSIONS
        for wagtail in WT_VERSIONS
        if not should_skip(python, django, wagtail)
    ],
)
def tests(session, django, wagtail):
    session.install("wagtail-heroicons[dev] @ .")

    if django == DJMAIN:
        session.install(
            "django @ https://github.com/django/django/archive/refs/heads/main.zip"
        )
    else:
        session.install(f"django=={django}")

    if wagtail == WTMAIN:
        session.install(
            "wagtail @ https://github.com/wagtail/wagtail/archive/refs/heads/main.zip"
        )
    else:
        session.install(f"wagtail=={wagtail}")

    session.run("python", "-m", "pytest")


@nox.session
def coverage(session):
    session.install("wagtail-heroicons[dev] @ .")
    session.run("python", "-m", "pytest", "--cov=wagtail_heroicons")

    try:
        summary = os.environ["GITHUB_STEP_SUMMARY"]
        with Path(summary).open("a") as output_buffer:
            output_buffer.write("")
            output_buffer.write("### Coverage\n\n")
            output_buffer.flush()
            session.run(
                "python",
                "-m",
                "coverage",
                "report",
                "--skip-covered",
                "--skip-empty",
                "--format=markdown",
                stdout=output_buffer,
            )
    except KeyError:
        session.run(
            "python", "-m", "coverage", "html", "--skip-covered", "--skip-empty"
        )

    session.run("python", "-m", "coverage", "report")


@nox.session
def lint(session):
    session.install("wagtail-heroicons[lint] @ .")
    session.run("python", "-m", "pre_commit", "run", "--all-files")


@nox.session
def mypy(session):
    session.install("wagtail-heroicons[dev] @ .")
    session.run("python", "-m", "mypy", ".")


@nox.session
def gha_matrix(session):
    sessions = session.run("nox", "-l", "--json", silent=True)
    matrix = {
        "include": [
            {
                "python-version": session["python"],
                "django-version": session["call_spec"]["django"],
                "wagtail-version": session["call_spec"]["wagtail"],
            }
            for session in json.loads(sessions)
            if session["name"] == "tests"
        ]
    }
    with Path(os.environ["GITHUB_OUTPUT"]).open("a") as fh:
        print(f"matrix={matrix}", file=fh)
