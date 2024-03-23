set dotenv-load := true

@_default:
    just --list

# ----------------------------------------------------------------------
# DEPENDENCIES
# ----------------------------------------------------------------------

bootstrap:
    @just pup
    python -m uv pip install --editable '.[dev]'

pup:
    python -m pip install --upgrade pip uv

# ----------------------------------------------------------------------
# TESTING/TYPES
# ----------------------------------------------------------------------

test *ARGS:
    python -m nox --session "test" -- "{{ ARGS }}"

testall *ARGS:
    python -m nox --session "tests" -- "{{ ARGS }}"

coverage:
    python -m nox --session "coverage"

types:
    python -m nox --session "mypy"

# ----------------------------------------------------------------------
# UTILS
# ----------------------------------------------------------------------

# format justfile
fmt:
    just --fmt --unstable

# run pre-commit on all files
lint:
    python -m nox --session "lint"
