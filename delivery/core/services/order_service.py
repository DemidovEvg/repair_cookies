import json

from django.conf import settings

from core.services import requests


class UpdateOrderStatus:
    elements_url = f"{settings.CLIENT_SERVICE}/api/orders/"
    element_url = elements_url + "{id}/"

    @classmethod
    def set_new_status(cls, order_id: str, new_status):
        url = cls.element_url.format(id=order_id)
        data = dict(status=new_status)
        headers = {"Content-type": "application/json"}
        print(
            f"Отправили запрос на обновление статуса заявки "
            f"{order_id} -> новый статус {new_status}"
        )
        response = requests.patch(url=url, data=json.dumps(data), headers=headers)
