import os
import logging
import string
import redis
import gevent
from flask import Flask, render_template,Blueprint
import flask_sockets
import codecs

def add_url_rule(self, rule, _, f, **options):
    self.url_map.add(flask_sockets.Rule(rule, endpoint=f, websocket=True))

flask_sockets.Sockets.add_url_rule = add_url_rule

REDIS_URL = os.environ['REDIS_URL']
REDIS_GAME = 'crown5'

app = Flask(__name__)

sockets = flask_sockets.Sockets(app)
redis = redis.from_url(REDIS_URL)

class GameStateUpdate:
  def __init__(self, room, message):
    self.room = room
    self.message = message
  
  def string(self) -> str:
      return f'{self.room}:{self.message}'

class GameBackend:
    """Interface for registering and updating WebSocket clients."""
    """TODO persisting game state for reconects"""
    def __init__(self):
        self.clients = [None]*9999
        self.pubsub = redis.pubsub()
        self.pubsub.subscribe(REDIS_GAME)

    def __iter_data(self):
        for message in self.pubsub.listen():
            data = message.get('data')
            if message['type'] == 'message':
                print(u'Sending message: {}'.format(data))
                yield data

    def register(self, client,room):
        """Register a WebSocket connection for Redis updates."""
        clientList = self.clients[room]
        if(clientList):
            clientList.append(client)
            self.clients[room] = clientList
        else:
            self.clients[room] = [client]

    def send(self, client, data):
        """Send given data to the registered client.
        Automatically discards invalid connections."""
        try:
            print(data)
            client.send(data)
        except ex:
            app.logger.info(ex)
            self.clients.remove(client)

    def run(self):
        """Listens for new messages in Redis, and sends them to clients."""
        for data in self.__iter_data():
            dataString = codecs.decode(data, 'UTF-8')
            print(data)
            print(dataString)
            room,message = dataString.split(":",1)
            roomClients = self.clients[int(room)]
            print(room,message)
            if(roomClients):
                for client in roomClients:
                    gevent.spawn(self.send, client, message)

    def start(self):
        """Maintains Redis subscription in the background."""
        gevent.spawn(self.run)

gameServer = GameBackend()
gameServer.start()

@app.route('/')
def hello():
    return render_template('index.html')

@sockets.route('/room/<room>', websocket=True)
def updates(ws,room):
    print(room)
    ws.send(room)
    gameServer.register(ws,int(room))
    while not ws.closed:
    # Sleep to prevent *contstant* context-switches.
        gevent.sleep(0.1)
        message = ws.receive()

        if message:
            print(u'Inserting message: {}'.format(message))
            update = GameStateUpdate(room,message)
            updateSting = update.string()
            print(u'Inserting message: {}'.format(updateSting))
            redis.publish(REDIS_GAME, updateSting)

