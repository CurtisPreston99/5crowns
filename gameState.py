import json 
import random
from unittest.util import three_way_cmp
from card import card

from commandHandler import commandHandler

class playerState:
    def __init__(self):
        self.score = 0
        self.cards:list[card] = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Encoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__
    
class crowns5GameState:

    def __init__(self):
        self.state= {
            'boardState':{'deck':[],'discard':[],'playersTurn':None},
            'playerState':[]
        }
        self.clients = []
        self.commandHandler = commandHandler()
    

    def addClient(self , client):
        self.clients.append(client)

    def addPlayer(self) -> int:
        player = playerState()
        self.state['playerState'].append(player)
        return len(self.state['playerState'])

    def getStateString(self) -> str:
        json_object = json.dumps(self.state, indent = 4, cls=Encoder) 
        return json_object
    
    def processMessage(self,message):
        print("message:"+message)
        messageDict = None
        try:
            messageDict = json.loads(message)
            self.state = self.commandHandler.handle(self.state,messageDict)
            return self.state
        except Exception as e:
            print("couldnt parse message:"+message)
            print(e)
            return self.state
        
        





