# Stage 1. builder
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

WORKDIR /docker_project

COPY ./src/pyproject.toml ./src/uv.lock ./

RUN uv sync --locked

COPY ./src/ .

# Stage 2. runtime
# FROM python:3.13-slim as runtime

# WORKDIR /docker_project

# COPY --from=builder /usr/local/bin/python3.13/site-packages /usr/local/bin/python3.13/site-packages
