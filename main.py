import logging

from fastapi import FastAPI
from fastapi.logger import logger

from app.events.routers.v1 import chapter_read

import logging
from fastapi.logger import logger as fastapi_logger

gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers

if __name__ != "__main__":
    fastapi_logger.setLevel(gunicorn_logger.level)
else:
    fastapi_logger.setLevel(logging.DEBUG)

app = FastAPI()

app.include_router(chapter_read.router)


@app.get("/")
async def root():
    return {"message": "In development"}
