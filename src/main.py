import pydantic
from bson.objectid import ObjectId
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI, Request
from loguru import logger
from loguru import logger as logging
from starlette.middleware.cors import CORSMiddleware

from src.db_wrapper import DbWrapper

load_dotenv(find_dotenv())

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()
db = DbWrapper()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://depremproje.com"],
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


@app.get("/get_users")
async def get_users():
    """
    :return: a list of all the latitudes and longitudes
    """
    try:
        logger.info("Get lat lon method was called.")

        return db.get_users()

    except Exception as e:
        logging.error(e)
        return e


@app.get("/get_users_lat_lon")
async def get_users_lat_lon():
    """
    :return: a list of all the latitudes and longitudes
    """
    try:
        logger.info("Get lat lon method was called.")

        return db.get_users_lat_lon()

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
        logger.info("Set lat lon method was called!!!!!!!!!")
        req = await info.json()

        return db.set_user_lat_lon(user_id=req["_id"], lat=req["lat"], lon=req["lon"])

    except Exception as e:
        logging.error(e)
        return e


@app.get("/get_user_parameters")
async def get_user_parameters(info: Request):
    """
    :param info: the user data to update
    :return: the updated user data
    """
    try:
        logger.info("Get user parameters method was called.")
        req = await info.json()

        return db.get_user_parameters(req)

    except Exception as e:
        logging.error(e)
        return e


@app.get("/select_options")
async def select_options():
    """
    :return: the updated user data
    """
    try:
        logger.info("Select options method was called.")

        return db.select_options()

    except Exception as e:
        logging.error(e)
        return e
