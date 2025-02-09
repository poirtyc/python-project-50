install:
	uv sync

run:
	uv run hexlet-python-package

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=. --cov-report=html --cov-report=term

test-coverage-term:
	uv run pytest --cov=. --cov-report=term-missing

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build