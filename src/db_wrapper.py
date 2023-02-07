import os

from dotenv import find_dotenv, load_dotenv
from fastapi import HTTPException
from loguru import logger
from pymongo import MongoClient

load_dotenv(find_dotenv())


class DbWrapper:
    def __init__(self):
        self.setup()

    def setup(self) -> bool:
        """
        :return: True if connected to the MongoDB, Error otherwise
        """
        try:
            self.connection_string = os.environ.get("MONGODB_PWD")
            self.client = MongoClient(self.connection_string)

            logger.info("Connected to MongoDB. Setup has completed.")

            return True

        except Exception as e:
            logger.error(e)
            return e

    def get_database_names(self):
        """
        :return: a list of all the database names
        """
        try:
            dbs = self.client.list_database_names()

            logger.info("Database names method was called.")

            return dbs

        except Exception as e:
            logger.error(e)
            return e

    def get_database(self, db_name: str):
        """
        :param db_name: the name of the database to get
        :return: the database object
        """
        try:
            db = self.client[db_name]

            logger.info("Database method was called.")

            return db

        except Exception as e:
            logger.error(e)
            return e

    def get_collections_names(self, db_name: str):
        """
        :param db_name: the name of the database to get the collections from
        :return: a list of all the collections in the database
        """
        try:
            db = self.get_database(db_name)
            collections = db.list_collection_names()

            logger.info("Collections names method was called.")

            return collections

        except Exception as e:
            logger.error(e)
            return e

    def get_collection(self, collection_name: str):
        """
        :param collection_name: the name of the collection to get
        :return: the collection object
        """
        try:
            db = self.get_database("deprem")
            collection = db[collection_name]

            logger.info("Collection method was called.")

            return collection

        except Exception as e:
            logger.error(e)
            return e

    def get_users(self):
        """
        :return: a list of all the users
        """
        try:
            collection = self.get_collection("users")

            logger.info("Get users method was called.")

            return collection.find()

        except Exception as e:
            logger.error(e)
            return e

    def set_user_lat_lon(self, user_data: dict, lat: float, lon: float):
        """
        :param user_data: the data of the user to insert
        :param lat: the latitude of the user
        :param lon: the longitude of the user
        :return: True if inserted, False otherwise
        """
        try:
            collection = self.get_collection("users")

            collection.update_one(
                {"_id": user_data["_id"]}, {"$set": {"lat": lat, "lon": lon}}
            )

            logger.info("Lat lon method was called successfully!")

            return HTTPException(
                status_code=200, detail="Lat lon method was called successfully!"
            )

        except Exception as e:
            logger.error(e)
            return e
