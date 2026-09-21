UV ?= uv

.PHONY: help setup format lint format-check typecheck test audit build check

help:
	@echo "make setup         Install Git hooks"
	@echo "make format        Apply Ruff lint fixes and formatting"
	@echo "make lint          Check Ruff lint rules"
	@echo "make format-check  Check formatting"
	@echo "make typecheck     Run Pyright"
	@echo "make test          Run tests with coverage"
	@echo "make audit         Audit dependencies"
	@echo "make build         Build wheel and source distribution"
	@echo "make check         Run all checks and build"

setup:
	$(UV) run pre-commit install --install-hooks

format:
	$(UV) run ruff check --fix .
	$(UV) run ruff format .

lint:
	$(UV) run ruff check .

format-check:
	$(UV) run ruff format --check .

typecheck:
	$(UV) run pyright

test:
	$(UV) run pytest --cov --cov-report=term-missing

audit:
	$(UV) run pip-audit

build:
	$(UV) build

check: lint format-check typecheck test audit build
