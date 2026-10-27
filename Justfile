ruff := "uv run ruff"
mypy := "uv run mypy"
pytest := "uv run pytest"

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

# Run tests
[group("Pytest")]
test:
    {{pytest}}

# Run tests with coverage
[group("Pytest")]
test-cov:
    {{pytest}} --cov

# Fix code style
[group("Quality")]
fix: lint-fix format

# Run static check
[group("Quality")]
check: lint format-check typecheck
check-ci: check test

image := "nexfix:local"
smoke_port := "18000"

# Build docker image
[group("Docker")]
docker-build:
    docker build -t {{image}} .

# Run app via docker compose
[group("Docker")]
up:
    docker compose up --build

# Stop docker compose services
[group("Docker")]
down:
    docker compose down

# Build image and check that the container starts and serves HTTP
[group("Docker")]
docker-smoke: docker-build
    #!/usr/bin/env bash
    set -euo pipefail
    test "$(docker run --rm {{image}} id -u)" = "10001" || { echo "container must not run as root"; exit 1; }
    cid=$(docker run -d --read-only --tmpfs /tmp --cap-drop=ALL --security-opt no-new-privileges \
        -p 127.0.0.1:{{smoke_port}}:8000 {{image}})
    trap 'docker rm -f "$cid" >/dev/null' EXIT
    for _ in $(seq 30); do
        if curl -fs http://127.0.0.1:{{smoke_port}}/openapi.json >/dev/null; then
            echo "Smoke test passed"
            exit 0
        fi
        sleep 1
    done
    docker logs "$cid"
    echo "Smoke test failed: app did not respond in 30s"
    exit 1
