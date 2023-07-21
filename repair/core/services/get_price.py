import json
import requests
from django.contrib import messages


def get_repair_price(category: str, repair_level: int, request):
    headers = {"Content-type": "application/json"}

    try:
        resp = requests.get("http://127.0.0.1:8000/api/prices/", headers=headers).content
        data = json.loads(resp)
        for el in data:
            if el['category'] == category and el['repairLvl'] == repair_level:
                return el['price']

    except Exception as exc:
        messages.add_message(request, messages.ERROR, repr(exc))

