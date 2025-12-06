from collections.abc import Iterable

from fastapi import APIRouter
from fastapi import FastAPI

from .endpoints.hello_world import hello_router


def create_app(routers: Iterable[APIRouter]) -> FastAPI:
    application = FastAPI(
        title='DevOps-Project',
        version='0.1.0',
        root_path='/api/v1'
    )

    for router in routers:
        application.include_router(router)

    return application


app = create_app(
    routers=(hello_router,),
)
