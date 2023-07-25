import asyncio
import json
import sys

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
        await self.accept()

    async def receive(self, text_data):
        if not self.client_data:
            client = await self.get_client(self.email)
            orders = await self.get_orders(client)
            self.client_data = await self.serialize_orders(orders)
            await self.send(text_data=json.dumps(self.client_data))

        while True:
            client = await self.get_client(self.email)
            orders = await self.get_orders(client)
            new_client_data = await self.serialize_orders(orders)
            if self.client_data != new_client_data:
                self.client_data = new_client_data
                await self.send(text_data=json.dumps(self.client_data))
            await asyncio.sleep(1)
