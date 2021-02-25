# coding: utf-8
import json
import time
from typing import Any
from typing import Dict
from typing import List
from typing import Text
import requests

unigloo_host = "https://bad-api-assignment.reaktor.com"
product_list_endpoint = "v2/products"  # Return a listing of products in a given category.
availability_endpoint = "v2/availability"  # Return a list of availability info.


def get_listing_of_product(category: Text) -> List[Dict[Text, Any]]:
    url = f"{unigloo_host}/{product_list_endpoint}/{category}"
    header = {"x-force-error-mode": "all"}

    result = requests.get(url=url, headers=header)

    if not result.status_code == 200:
        raise AssertionError(f"Expected HTTP code 200, but got {result.status_code}")

    products = json.loads(result.content)

    return products


def get_availability(manufacturer: Text) -> List[Dict[Text, Text]]:
    url = f"{unigloo_host}/{availability_endpoint}/{manufacturer}"
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        result = requests.get(url=url)
        response = json.loads(result.content)['response']
        if not result.status_code == 200:
            raise AssertionError(f"Expected HTTP code 200, but got {result.status_code}")

        if type(response) != str:
            break

        time.sleep(1 ** attempts)
        attempts = attempts + 1

    return response
