import json
import requests


def get_repir_price(cat: str, rprplvl: int):
    headers = {"Content-type": "application/json"}
    resp = requests.get("http://127.0.0.1:8000/api/prices/", headers=headers).content
    a = json.loads(resp)
    for el in a:
        if el['category'] == cat and el['repairLvl'] == rprplvl:
            return el['price']
