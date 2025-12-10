#!/bin/bash

set -e

if [ "$ENVIRONMENT" = 'dev' ]; then
    echo "Running Development Server"
    exec uvicorn \
        --host=0.0.0.0 \
        --port=8000 \
        backend.infrastructure.entrypoints.rest_api:fastapi_app \
        --reload \
        --log-level debug \
        --use-colors
else
    echo "Running Production Server"
    exec uvicorn \
        --host=0.0.0.0 \
        --port=8000 \
        backend.infrastructure.entrypoints.rest_api:fastapi_app
fi
