import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        'infrastructure.entrypoints.rest_api:fastapi_app',
        port=8080,
        reload=True,
        log_level='debug',
        use_colors=True,
    )
