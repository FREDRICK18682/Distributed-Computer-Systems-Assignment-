#to create a websocket consumer
#the channel websocke consumer for a real_time application
#handels connection, disconnection, incoming massages from users and brodcast messages to 
# everyone in the same chart room
# (even when the application is running on multiple server nodes usinbg Redis)
#consumer fil handerws vares activity such as 
# a) user join ing the room
# b) user leave the room.
# c) a application receive messages from websocket client
# d) user sending messages to the room group
#    (broadcasting to Node A, node B etc via Redis)
# e) Receive messags from the group
#   (triggered by Redis)
# f) Sebnding messages back to websocket  client

import json
from channels.generic.websocket import AsyncWebsocketConsumer
class ChartConsumer(AsyncWebsocketConsumer):
    # async keyword are used before def to define an asynchronous function(coroutine)
    async def connect(self):
       #Extracte cthe room name from the URL
        self.Chart_Room = self.scope['url_route']['kwargs']['chart_Room']
        #creating a unique Group name
        self.Chart_Room=f'chart_{self.Chart_Room}'
        #join room group(Redis syncs this  across multiple server nodes)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
		)
        await self.accept()
        return await super().connect()
    