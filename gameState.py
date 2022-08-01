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
            'boardState':{'messageC':0},
            'playerState':[]
        }
        self.clients = []
    
    def addClient(self , client):
        self.clients.append(client)

    def addPlayer(self) -> int:
        player = playerState()
        self.state['playerState'].append(player)
        return len(self.state['playerState'])

    def getStateString(self) -> str:
        json_object = json.dumps(self.state, indent = 4, cls=Encoder) 
        return json_object
    
    def parseMessage(self,message):
        self.state['boardState']['messageC'] += 1
        return message;


class playerState:
    def __init__(self):
        self.score = 0
        self.card = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Encoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__