import json 
import random

class card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

class playerState:
    def __init__(self):
        self.score = 0
        self.cards = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Encoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__

suits = [
    "Hearts",
    "Diamonds",
    "Clovers",
    "Spades",
    "Stars"
]

cards = []

for i in suits:
    for e in range(3,13):
        cards.append(card(i,e))
    
class crowns5GameState:
    def __init__(self):
        self.state = {
            'boardState':{'deck':[]},
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
        print("message:"+message)
        # messageDict = json.loads(message)
        self.startRound()
        # if messageDict['command']=="start":
        return message
        
    def startRound(self,round = 0):
        nCards = round + 3

        deck = cards.copy()
        deck = [deck,deck]

        deck = [item for sublist in deck for item in sublist]

        for i in range(6):
            deck.append(card(None,50))

        random.shuffle(deck)
        
        self.state['deck'] = deck




