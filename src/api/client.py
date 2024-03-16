import json
import logging

import requests

# TODO: build Pydantic models for all of these responses


def getAvalancheData():
    """Return the raw JSON response from CAIC all avalanche products API"""

    url = "https://avalanche.state.co.us/api-proxy/avid"
    params = {"_api_proxy_uri": "/products/all?includeExpired=true"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Request failed with status code: {response.status_code}")
        return None


def getAvalancheForecasts(avi_data: dict):
    """Return a list of all available avalanche forecasts"""
    return [f for f in avi_data if f["type"] and f["type"] == "avalancheforecast"]


def getDangerRatingByDay(forecast: dict, i: int = 0) -> dict:
    """
    Returns a formatted string for the danger rating.
    Contains a 3 element list where [today, tomorrow, day_after]
    By default returns the current day (first element)
    """
    print(json.dumps(forecast["dangerRatings"]["days"][i], indent=2))


def getAvalancheProblemsByDay(forecast: dict, i: int = 0) -> list[dict]:
    """
    Returns a formatted string for the avalanche problem(s).
    Contains a 3 element list where [today, tomorrow, day_after]
    By default returns the current day (first element)
    """
    print(json.dumps(forecast["avalancheProblems"]["days"][i], indent=2))
