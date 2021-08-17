import json
from random import randint
from time import sleep

from channels.db import database_sync_to_async
# from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from polls.models import Comment


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(5):
            self.send(
                json.dumps({'message': randint(1, 100)})
            )
            sleep(4)


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connect')
        self.testrun_id = self.get_kwarg('pk')
        self.group_name = f'testrun_{self.testrun_id}'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    def get_kwarg(self, key):
        return self.scope['url_route']['kwargs'][key]

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        comment = data['text']

        new_comment = await self.save_comment(self.testrun_id, comment)
        data = {
            'author': new_comment.user.username,
            'created_at': new_comment.created_at.strftime('%Y-%m-%d'),
            'text': new_comment.text
        }

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'new.comment',
                'message': data,
            }
        )

    @database_sync_to_async
    def save_comment(self, testrun_id, text):
        return Comment.objects.create(
            user=self.scope['user'],
            text=text,
            testrun_id=testrun_id
        )

    async def new_comment(self, event):
        message = event['message']
        print('new_comment event is got')

        await self.send(
            text_data=json.dumps({'message': message})
        )