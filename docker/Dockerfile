FROM python:3.13-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /docker_project

COPY ./src/pyproject.toml ./src/uv.lock ./

RUN uv sync --locked

COPY ./src/ .

ENV PATH="/docker_project/.venv/bin:$PATH"

WORKDIR /docker_project/backend

CMD ["uv","run", "uvicorn", "--host=0.0.0.0", "--port=8000", "infrastructure.entrypoints.rest_api:fastapi_app"]
