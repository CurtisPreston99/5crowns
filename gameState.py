import json 
import random
from unittest.util import three_way_cmp
from card import card
import uuid
import redis

from commandHandler import commandHandler

class playerState:
    def __init__(self):
        self.score = 0
        self.id = str(uuid.uuid4())
        self.name = ""
        self.cards:list[card] = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Encoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__
    
class crowns5GameState:

    def __init__(self,roomNumber,redisConnection):
        state= {
            'boardState':{'deck':[],'discard':[],'playersTurn':None},
            'playerState':[]
        }
        self.clients = []
        self.commandHandler = commandHandler()
        self.redis = redisConnection
        self.redisKey = "gameState:"+str(roomNumber)
        self.redis.setex(self.redisKey,43200,self.getStateString(state))

    def addClient(self , client):
        self.clients.append(client)

    def addPlayer(self) -> int:
        # todo use redis
        state = self.getState()
        player = playerState()
        state['playerState'].append(player)
        self.setState(state)
        return len(state['playerState']),player.id

    def getStateString(self,state) -> str:
        json_object = json.dumps(state, indent = 4, cls=Encoder) 
        return json_object
    
    def getStateStringFromReddis(self) -> str:
        state = self.getState()
        json_object = json.dumps(state, indent = 4, cls=Encoder) 
        return json_object
    
    def getState(self):
        redisState = self.redis.get(self.redisKey)
        parseState = json.loads(redisState)
        return parseState
    
    def setState(self,state):
        stateString = self.getStateString(state)
        self.redis.setex(self.redisKey,43200,stateString)
        
    def processMessage(self,message):
        messageDict = None
        try:
            messageDict = json.loads(message)
            state = self.commandHandler.handle(self.getState(),messageDict)
            return state
        except Exception as e:
            print("couldnt parse message:"+message)
            print(e)
            return self.getState()
        
        





