import requests
from core.api_auth import headers_with_token, remove_api_token


def get(url, params=None, **kwargs):
    return make_request('get', url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):
    return make_request('post', url, data=data, json=json, **kwargs)

def patch(url, data=None, **kwargs):
    return make_request('patch', url, data=data, **kwargs)

def put(url, data=None, **kwargs):
    return make_request('put', url, data=data, **kwargs)

def delete(url, **kwargs):
    return make_request('delete', url, **kwargs)

def make_request(action, url, params=None, headers=None, **kwargs: dict):
    if not headers:
        headers = {}
    response = requests.request(action, url=url, params=params, headers=headers_with_token(headers), **kwargs)
    if response.status_code == 403:
        remove_api_token()
        response = requests.request(action, url=url, params=params, headers=headers_with_token(headers), **kwargs)
    return response
