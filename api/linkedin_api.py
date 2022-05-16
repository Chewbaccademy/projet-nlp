import requests


def auth(url, headers, data):
    """
    Function that makes a request to the LinkedIn API to get the access token.
    """
    
    response = requests.post(url, headers=headers, data=data)
    return response.json()