# pytemplate

A minimal Python 3.12+ template with a `src/` layout,
[uv](https://docs.astral.sh/uv/), [Hatchling](https://hatch.pypa.io/),
[Ruff](https://docs.astral.sh/ruff/), [Pyright](https://github.com/microsoft/pyright),
[pytest](https://docs.pytest.org/), and
[GitHub Actions](https://docs.github.com/en/actions). No runtime dependencies.

## Setup

With [`uv`](https://docs.astral.sh/uv/getting-started/installation/) and
[`make`](https://swcarpentry.github.io/make-novice/#gnu-make) installed, run:

```sh
make setup      # Install pre-commit and commit-msg hooks
make test       # Run tests with coverage
```

## Example

The package includes a simple recursive Fibonacci function:

```python
from pytemplate.fibonacci import fibonacci

print(fibonacci(10))  # 55
```

Indices start at zero. Negative indices raise `ValueError`; use small inputs
because this example repeats recursive work.

## Development

```sh
make            # List targets
make format     # Apply Ruff lint fixes and formatting
make typecheck  # Type checking
make test       # Tests with coverage and uncovered lines
make audit      # Dependency audit
make build      # Wheel and source archive in dist/
make check      # Lint, formatting check, types, tests, audit, and build
```

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):
`type(scope): description`, with an optional scope.

```text
feat: add configuration loader
fix(config): handle missing settings
docs: update setup instructions
feat(api)!: remove deprecated endpoint
```

Allowed types: `build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`,
`revert`, `style`, `test`. Use `!` for breaking changes. Merge and fixup messages
must also follow this format.

## Customize

- Rename `src/pytemplate/` and update its references in `pyproject.toml` and tests.
- Replace the package description, README, example module, and tests.
- Add dependencies in `pyproject.toml`, run `uv sync`, and commit `uv.lock`.
- Keep Python versions aligned in `.python-version` and `pyproject.toml`.
- When upgrading Ruff, update its dependency pin, `required-version`, and
  `.pre-commit-config.yaml` revision together. Use the project’s Ruff in your editor.

## License

Licensed under the [Apache License 2.0](LICENSE).
