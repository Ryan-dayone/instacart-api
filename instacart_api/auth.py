"""

Author: Ryan Morlando
Created: 
Updated: 
V1.0.0
Patch Notes:

To Do:

"""
import requests
import json
from os import environ as env


def get_token(authorization_code):
    """
    only called when app is first authorized to get the refresh token. That refresh token will be used to get all
    access tokens in the future through refresh_token(). Please add the refresh token to the .env file
    to get the authorization code. Please follow the steps in the instacart documentation.
    The refresh token issued will be used in the refresh_token() method to get a new access token.
    Youll need to add it to the enviroment variable as: {client}_instacart_refresh_token
    :param authorization_code: from instacart portal. Authorize app and copy code in url
    :return:
    """

    url = "https://api.ads.instacart.com/oauth/token"

    payload = json.dumps({
        "client_id": f"{env.get('instacart_client_id')}",
        "client_secret": f"{env.get('instacart_client_secret')}",
        "redirect_uri": "https://127.0.0.1",
        "code": f"{authorization_code}",
        "grant_type": "authorization_code"
    })

    headers = {
        "content-type": "application/json"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        print('Authentication token fetch successful. please add both to .env file')
        # set the key as an environment variable
        print(f"Access Token:{json.loads(response.text)['access_token']}")
        print(f"Refresh Token:{json.loads(response.text)['refresh_token']}")
        exit("Please add the above to .env file")

    else:
        exit(f'{response.text}')


def refresh_token():
    """
    gets the refresh token
    :return:
    """
    if 'instacart_refresh_token' not in env:
        exit('Use get_token() and save the Refresh Token in .env file')

    url = "https://api.ads.instacart.com/oauth/token"

    payload = json.dumps({
        "client_id": f"{env.get('instacart_client_id')}",
        "client_secret": f"{env.get('instacart_client_secret')}",
        "redirect_uri": "https://127.0.0.1",
        "refresh_token": f"{env.get('instacart_refresh_token')}",
        "grant_type": "refresh_token"
    })
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        print('Authentication token fetch successful')

        # set the api token as an environment variable
        env.__setitem__(key='instacart_access_token', value=str(json.loads(response.text)['access_token']))

    else:
        exit(f'{response.text}')
