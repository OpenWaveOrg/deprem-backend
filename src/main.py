from loguru import logger
from bson.objectid import ObjectId
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from loguru import logger as logging
import pydantic

from db_wrapper import DbWrapper

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root(info: Request):
    """
    :return: a welcoming screen
    """
    try:
        logger.info("Root method was called.")

        return "Deprem Projesi API"

    except Exception as e:
        logging.error(e)
        return e
