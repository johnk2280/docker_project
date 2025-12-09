FROM python:3.13-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /docker_project

COPY ./src/pyproject.toml ./src/uv.lock ./

RUN groupadd -r app_group && useradd -r -g app_group app_user

# ---
# install dependencies to .venv into docker container
# RUN uv sync --locked

# install dependencies to system environment into docker container
RUN uv pip install --system --no-cache-dir -r pyproject.toml  

COPY ./src/ .

EXPOSE 8000

USER app_user

# when install dependencies to .venv
# ENV PATH="/docker_project/.venv/bin:$PATH"

WORKDIR /docker_project/backend

# when install dependencies to .venv
# CMD ["uv","run", "uvicorn", "--host=0.0.0.0", "--port=8000", "infrastructure.entrypoints.rest_api:fastapi_app"]

# when install dependencies to system environment
CMD ["uvicorn", "--host=0.0.0.0", "--port=8000", "infrastructure.entrypoints.rest_api:fastapi_app", "--reload"]
