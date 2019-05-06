import random
import card

class Deck(object):

    def __init__(self): #constructs deck and shuffles
        self.deck=list()
        self.pointer=-1
        for suit in range(1,5):
            for rank in range(1, 14):
                self.deck.append(card.Card(rank,suit))
        random.shuffle(self.deck)
        return None

    def getDeck(self): #returns deck object
        return self

    def showEntireDeck(self): #returns printable version of the entire deck = debugging only
        printableDeck = list()
        for x in range(len(self.deck)):
            printableDeck.append([self.deck[x].getNumber(),self.deck[x].getSuit()])
        return printableDeck


    def giveNextCard(self): #advances deck pointer by one and returns next card
        self.pointer+=1
        return self.deck[self.pointer]


'''
d = Deck()
print(d.showEntireDeck())
currentCard = d.getDeck().giveNextCard()
print(currentCard.getNumber(),currentCard.getSuit())
currentCard = d.getDeck().giveNextCard()
print(currentCard.getNumber(),currentCard.getSuit())
'''



