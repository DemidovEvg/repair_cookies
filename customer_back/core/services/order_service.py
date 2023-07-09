import json

from core.services import requests


def create_or_update(service_create: str, service_update: str, data: dict):
    headers = {"Content-type": "application/json"}

    response = requests.get(url=service_update)
    if response.status_code == 200:
        response = requests.patch(url=service_update, data=json.dumps(data), headers=headers)
    elif response.status_code == 404:
        response = requests.post(url=service_create, data=json.dumps(data), headers=headers)
    else:
        raise Exception(response.text)

    if response.status_code > 299:
        raise Exception(response.text)
