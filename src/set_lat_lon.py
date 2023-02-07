import ast

import pydantic
import requests
from bson.objectid import ObjectId
from loguru import logger

from db_wrapper import DbWrapper

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


db = DbWrapper()

all_addresses = db.get_users()

for i in all_addresses:
    try:
        address = f"{i['konum_il'], i['konum_ilce'], i['konum_mahalle'], i['adres']}"
        address = ast.literal_eval(address)
        address = " ".join(address)

        logger.info(f"Address: {address}")

        req = requests.get(
            f"https://public-sdc.trendyol.com/discovery-web-websfxgeolocation-santral/geocode",  # noqa F841
            params={"address": address},
        )

        if req.status_code == 200:
            req = req.json()

            if req["results"]:
                logger.info("Lat lon method was called successfully!")

                requests.post(
                    "http://localhost:8000/set_user_lat_lon",
                    json={
                        "user_data": {"_id": str(i["_id"])},
                        "lat": req["results"][0]["geometry"]["location"]["lat"],
                        "lon": req["results"][0]["geometry"]["location"]["lng"],
                    },
                )
            else:
                logger.info("Lat lon method was failed!")

                requests.post(
                    "http://localhost:8000/set_user_lat_lon",
                    json={"user_data": {"_id": str(i["_id"])}, "lat": "", "lon": ""},
                )
        else:
            logger.info("Lat lon method was failed!!!!!!")

            requests.post(
                "http://localhost:8000/set_user_lat_lon",
                json={"user_data": {"_id": str(i["_id"])}, "lat": "", "lon": ""},
            )

    except Exception as e:
        logger.error(e)
        continue
