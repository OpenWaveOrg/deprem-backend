import pydantic
from bson.objectid import ObjectId
from fastapi import FastAPI, Request
from loguru import logger
from loguru import logger as logging
from starlette.middleware.cors import CORSMiddleware

from db_wrapper import DbWrapper

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()
db = DbWrapper()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


@app.get("/get_user")
async def get_user():
    """
    :return: a list of all the latitudes and longitudes
    """
    try:
        logger.info("Get lat lon method was called.")

        return db.get_lat_lon()

    except Exception as e:
        logging.error(e)
        return e


@app.post("/set_user_lat_lon")
async def set_user_lat_lon(info: Request):
    """
    :param info: the user data to update
    :return: the updated user data
    """
    try:
        logger.info("Set lat lon method was called.")
        req = await info.json()

        return db.set_user_lat_lon(req["user_data"], req["lat"], req["lon"])

    except Exception as e:
        logging.error(e)
        return e
