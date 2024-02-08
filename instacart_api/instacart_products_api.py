"""

Author: Ryan Morlando
Created: 
Updated: 
V1.0.0
Patch Notes:

To Do:

"""
from instacart_api import auth
import json
import requests
from os import environ as env
import pandas as pd


api_endpoint = "https://api.ads.instacart.com/api/v2/"


def get_product_mapping():
    url = f"{api_endpoint}products/product_mapping"

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {env.get("instacart_access_token")}'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        print('Products Fetched')
        return json.loads(response.text)
    elif response.status_code == 401:
        print('Refreshing Token')
        auth.refresh_token()
        return get_product_mapping()
    else:
        print(response.status_code)
        return pd.DataFrame()


def get_targeting_options():
    url = f"{api_endpoint}targeting/options"

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {env.get("instacart_access_token")}'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        print('Products Fetched')
        return json.loads(response.text)
    elif response.status_code == 401:
        print('Refreshing Token')
        auth.refresh_token()
        return get_product_mapping()
    else:
        print(response.status_code)
        return pd.DataFrame()