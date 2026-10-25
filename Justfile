ruff := "uv run ruff"
mypy := "uv run mypy"

default:
    @just --list

# Check lint errors
[group("Ruff")]
lint:
    {{ruff}} check .

# Fix lint errors
[group("Ruff")]
lint-fix:
    {{ruff}} check --fix .

# Format code
[group("Ruff")]
format:
    {{ruff}} format .

# Check formatting
[group("Ruff")]
format-check:
    {{ruff}} format --check .

# Checks type
[group("Mypy")]
typecheck:
    {{mypy}} src

# Fix code style
[group("Quality")]
fix: lint-fix format

# Run static check
[group("Quality")]
check: lint format-check typecheck
check-ci: check