import json 
import random
from unittest.util import three_way_cmp

from card import card

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
class commandHandler:
    def __init__(self):
        self.route = {
            'startGame':self.init,
            'takeFromDeck':self.takeFromDeck,
            'takeFromDiscard':self.takeFromDiscard,
            'setPlayer':self.setPlayer,
        }
    
    def handle(self,state,command):
        type = command['comandType']
        args = command['params']
        func=self.route[type]
        print(type)
        print(func)
        return func(state,args)
    
    def setPlayer(self,state,args):
        id = args['id']
        name = args['name']

        players = state['playerState']

        for index, item in enumerate(players):
            if item['id'] == id:
                break
            else:
                index = -1
        
        item['name'] = name
        state['playerState'][index] = item

        return state


    def takeFromDiscard(self,state,args):
        currentPlayer= state['playersTurn']
        newCard = state['boardState']['discard'][0]
        newDiscard = state['boardState']['discard'][1:]
        state['playerState'][currentPlayer]['cards'].append(newCard)
        state['boardState']['discard'] = newDiscard
        return state
    
    def takeFromDeck(self,state,args):
        currentPlayer= state['playersTurn']
        newCard = state['boardState']['deck'][0]
        newDeck = state['boardState']['deck'][1:]
        state['playerState'][currentPlayer]['cards'].append(newCard)
        state['boardState']['deck'] = newDeck
        return state
    
    def init(self,state,args):
        for player in state['playerState']:
            player['score'] = 0

        state['playersTurn'] = 0
        return self.startRound(state,0)

    def startRound(self,state,round = 0):
        nCards = round + 3

        deck = cards.copy()
        deck = [deck,deck]

        deck = [item for sublist in deck for item in sublist]

        for i in range(6):
            deck.append(card(None,50))
        
        random.shuffle(deck)

        for player in state['playerState']:
            player['cards'] = deck[0:nCards]
            deck = deck[nCards:]
        
        state['boardState']['deck'] = deck[1:]
        state['boardState']['discard'] = [deck[1]]
        return state
