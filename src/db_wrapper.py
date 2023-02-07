import os
from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient
from loguru import logger

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
            db = self.get_database("users")
            collection = db[collection_name]

            logger.info("Collection method was called.")

            return collection

        except Exception as e:
            logger.error(e)
            return e
