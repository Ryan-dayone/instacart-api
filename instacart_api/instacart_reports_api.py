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
from time import sleep
import pandas as pd
from io import StringIO


api_endpoint = "https://api.ads.instacart.com/api/v2/reports/"


def request_report(report_type: str, start_date, end_date):
    url = f"{api_endpoint}{report_type}"

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {env.get("instacart_access_token")}'
    }

    payload = json.dumps({
      "date_range": {
        "start_date": f"{start_date}",
        "end_date": f"{end_date}"
      },
      "segment": "day",
      "attribution_model": "last_touch",
      "name": f"{report_type}",
      "exclude_fields": ["roas", "ctr", "average_cpc"]
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 202:
        print(f'{report_type} report request successful')
        return json.loads(response.text)

    elif response.status_code == 401:
        print('Refreshing Token')
        auth.refresh_token()
        return request_report(report_type=report_type, start_date=start_date, end_date=end_date)

    else:
        exit(f'{response.text}')


def is_generated(report_id: str):
    url = f"{api_endpoint}{report_id}"

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {env.get("instacart_access_token")}'
    }
    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        print('File Generated')
        return True
    elif response.status_code == 202:
        print('Still Pending, trying again in 30 seconds')
        sleep(30)
        return is_generated(report_id=report_id)

    elif response.status_code == 401:
        print('Refreshing Token')
        auth.refresh_token()
        return is_generated(report_id=report_id)
    else:
        print(response.status_code)
        return False


def download_report(report_id: str):
    url = f"{api_endpoint}{report_id}/download"

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {env.get("instacart_access_token")}'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        print('File Downloaded')
        return pd.read_csv(StringIO(response.text), dtype=str)
    elif response.status_code == 401:
        print('Refreshing Token')
        auth.refresh_token()
        return download_report(report_id=report_id)
    else:
        print(response.status_code)
        return pd.DataFrame()
