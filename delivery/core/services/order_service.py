import json

from core.services import requests


def create_or_update(service_create: str, service_update: str, data: dict):
    headers = {"Content-type": "application/json"}
    response = requests.patch(
        url=service_update, data=json.dumps(data), headers=headers
    )
    if response.status_code > 299:
        raise Exception(response.text)
