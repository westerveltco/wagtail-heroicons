set dotenv-load := true

@_default:
    just --list

[private]
nox SESSION *ARGS:
    uv run nox --session "{{ SESSION }}" -- "{{ ARGS }}"

bootstrap:
    uv sync --locked

download:
    python -m download

lock *ARGS:
    uv lock {{ ARGS }}

# ----------------------------------------------------------------------
# TESTING/TYPES
# ----------------------------------------------------------------------

test *ARGS:
    @just nox test {{ ARGS }}

testall *ARGS:
    @just nox tests {{ ARGS }}

coverage:
    @just nox coverage

types:
    @just nox mypy

# ----------------------------------------------------------------------
# UTILS
# ----------------------------------------------------------------------

# format justfile
fmt:
    just --fmt --unstable

# run prek on all files
lint:
    @just nox lint
