import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from core.models import Client
from core.serializers import OrderModelSerializer


class ClientConsumer(AsyncJsonWebsocketConsumer):
    @database_sync_to_async
    def get_client(self, email):
        return Client.objects.filter(email=email).first()

    @database_sync_to_async
    def get_orders(self, client: Client):
        return client.orders.all()

    @database_sync_to_async
    def serialize_orders(self, orders):
        return OrderModelSerializer(
            instance=orders,
            many=True,
        ).data

    async def connect(self):
        self.email = self.scope["url_route"]["kwargs"]["email"]
        self.client = await self.get_client(self.email)
        if not self.client:
            raise Exception(f"No client with {self.email}")
        self.client_data = None
        await self.channel_layer.group_add(
            f"sync_client_orders_channel_group_{self.client.id.hex}", self.channel_name
        )
        self.groups.append(f"sync_client_orders_channel_group:{self.client.id.hex}")

        await self.accept()

    async def receive(self, text_data):
        client = await self.get_client(self.email)
        orders = await self.get_orders(client)
        self.client_data = await self.serialize_orders(orders)
        await self.send(text_data=json.dumps(self.client_data))
