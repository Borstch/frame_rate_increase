import logging

import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware

import config
from api.api import router

logger = logging.getLogger("increaser")

tags_metadata = [
    {
        "name": "image",
        "description": "Methods for increasing frame rate of a video file",
    },
    {
        "name": "video",
        "description": "Methods for getting image between two given frames",
    },
]


def format_long_message(message: dict) -> dict:
    result = dict(message)
    for key in result.keys():
        if (
            isinstance(result[key], str)
            and len(result[key]) > config.MAX_MESSAGE_LENGTH
        ):
            result[key] = (
                result[key][: config.MAX_MESSAGE_LENGTH // 4]
                + "..."
                + result[key][-(config.MAX_MESSAGE_LENGTH // 4) :]
            )
        elif isinstance(result[key], dict):
            result[key] = format_long_message(result[key])

    return result


async def log_request_json(request: Request) -> None:
    params = {**request.path_params, **request.query_params}
    body = {}
    content_type = request.headers.get("Content-Type")
    if not config or content_type.startswith("application/json"):
        body = await request.json() if await request.body() else {}

    req = f"{request.client.host} {request.method} {request.url.path}"
    logger.info(f"Request {req} params: {params}, body: {format_long_message(body)}")


app = FastAPI(
    debub=config.DEBUG,
    title=config.APP_TITLE,
    version=config.APP_VERSION,
    description=config.API_DESCR,
    redoc_url=None,
    openapi_tags=tags_metadata,
)

app.include_router(router, dependencies=[Depends(log_request_json)])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=80,
        workers=config.APP_WORKERS,
        debug=config.DEBUG,
        access_log=config.ACCESS_LOG,
        log_level=config.LOG_LEVEL,
        log_config=config.LOGGING_CONFIG,
    )
