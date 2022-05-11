import os
import logging
import string
import redis
import gevent
from flask import Flask, render_template,Blueprint
import flask_sockets

def add_url_rule(self, rule, _, f, **options):
    self.url_map.add(flask_sockets.Rule(rule, endpoint=f, websocket=True))

flask_sockets.Sockets.add_url_rule = add_url_rule

REDIS_URL = os.environ['REDIS_URL']
REDIS_CHAN = 'chat'
REDIS_GAME = 'game'

app = Flask(__name__)

sockets = flask_sockets.Sockets(app)
redis = redis.from_url(REDIS_URL)

class GameStateUpdate:
  def __init__(self, room, message):
    self.room = room
    self.message = message
  
  def string(self) -> str:
      return f'{self.room}:{self.message}'


class ChatBackend(object):
    """Interface for registering and updating WebSocket clients."""

    def __init__(self):
        self.clients = list()
        self.pubsub = redis.pubsub()
        self.pubsub.subscribe(REDIS_CHAN)

    def __iter_data(self):
        for message in self.pubsub.listen():
            data = message.get('data')
            if message['type'] == 'message':
                app.logger.info(u'Sending message: {}'.format(data))
                yield data

    def register(self, client):
        """Register a WebSocket connection for Redis updates."""
        self.clients.append(client)

    def send(self, client, data):
        """Send given data to the registered client.
        Automatically discards invalid connections."""
        try:
            client.send(data)
        except Exception:
            self.clients.remove(client)

    def run(self):
        """Listens for new messages in Redis, and sends them to clients."""
        for data in self.__iter_data():
            for client in self.clients:
                gevent.spawn(self.send, client, data)

    def start(self):
        """Maintains Redis subscription in the background."""
        gevent.spawn(self.run)


class GameBackend(object):
    """Interface for registering and updating WebSocket clients."""

    def __init__(self):
        self.clients = [None]*9999
        self.pubsub = redis.pubsub()
        self.pubsub.subscribe(REDIS_GAME)

    def __iter_data(self):
        for message in self.pubsub.listen():
            data = message.get('data')
            if message['type'] == 'message':
                app.logger.info(u'Sending message: {}'.format(data))
                yield data

    def register(self, client,room):
        """Register a WebSocket connection for Redis updates."""
        self.clients[room]=client

    def send(self, client, data):
        """Send given data to the registered client.
        Automatically discards invalid connections."""
        try:
            client.send(data)
        except ex:
            app.logger.info(ex)
            self.clients.remove(client)

    def run(self):
        """Listens for new messages in Redis, and sends them to clients."""
        for data in self.__iter_data():
            roomClients = self.clients[data.room]
            for client in roomClients:
                gevent.spawn(self.send, client, data)

    def start(self):
        """Maintains Redis subscription in the background."""
        gevent.spawn(self.run)

gameServer = GameBackend()
gameServer.start()

@app.route('/')
def hello():
    return render_template('index.html')

@sockets.route('/submit', websocket=True)
def inbox(ws):
    """Receives incoming chat messages, inserts them into Redis."""
    while not ws.closed:
        # Sleep to prevent *contstant* context-switches.
        gevent.sleep(0.1)
        message = ws.receive()

        if message:
            app.logger.info(u'Inserting message: {}'.format(message))
            redis.publish(REDIS_CHAN, message)

@sockets.route('/receive', websocket=True)
def outbox(ws):
    """Sends outgoing chat messages, via `ChatBackend`."""
    chats.register(ws)

    while not ws.closed:
        # Sleep to prevent *contstant* context-switches.
        gevent.sleep(0.1)
        message = ws.receive()

        if message:
            app.logger.info(u'Inserting message: {}'.format(message))
            redis.publish(REDIS_CHAN, message)

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
            app.logger.info(u'Inserting message: {}'.format(message))
            update = GameStateUpdate(room,message)
            updateSting = update.string()
            app.logger.info(u'Inserting message: {}'.format(updateSting))
            redis.publish(REDIS_GAME, updateSting)

