import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENCAGE_API_KEY")

BASE_URL = "https://api.opencagedata.com/geocode/v1/json"


def geocode_address(address):
    """
    Gjør en adresse/stedsnavn om til koordinater
    ved hjelp av OpenCage.
    """

    if not API_KEY:
        raise ValueError(
            "OPENCAGE_API_KEY mangler i .env-filen."
        )

    params = {
        "q": address,
        "key": API_KEY,
        "countrycode": "no",
        "limit": 1
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return None

    result = data["results"][0]

    return {
        "latitude": result["geometry"]["lat"],
        "longitude": result["geometry"]["lng"],
        "formatted": result.get("formatted")
    }
