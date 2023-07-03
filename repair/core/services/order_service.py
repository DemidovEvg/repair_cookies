import json

from core.services import requests


def update_outer_order(service_update: str, data: dict):
    headers = {"Content-type": "application/json"}

    response = requests.get(url=service_update)
    if response.status_code == 200:
        response = requests.patch(url=service_update, data=json.dumps(data), headers=headers)
    else:
        raise Exception(response.text)
    if response.status_code > 299:
        raise Exception(response.text)
