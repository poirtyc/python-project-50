install:
	uv sync

run:
	uv run hexlet-code

test:
	uv run pytest

test-cov:
	uv run pytest --cov=gendiff --cov-report=term-missing

test-coverage:
	pytest --cov=gendiff --cov-report=xml

lint:
	uv run ruff check

check: test lint

build:
	uv build