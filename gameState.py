import json 

cards = []
for i in range(0,5):
    type = []
    for e in range(3,13):
        type.append(e)
    cards.append(type)
    
CLOVER = 0
HEART = 1
SPADES = 2
STARS = 3
DIAMONDS = 4

class crowns5GameState:
    def __init__(self):
        self.state = {
            'boardState':{},
            'playerState':[]
        }
        self.clients = []
    
    def addClient(self , client):
        self.clients.append(client)

    def addPlayer(self) -> int:
        player = playerState()
        self.state.playerState.append(player)
        return len(self.state.playerState)

    def getStateString(self,playerNum) -> str:
        json_object = json.dumps(self.state, indent = 4) 
        return json_object
    
    def parseMessage(self,message):
        return message;


class playerState:
    def __init__(self):
        self.score = 0
        self.card = []

