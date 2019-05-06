import card
class Player(object):

    def __init__(self,cash):
        self.cash=cash
        self.hand=list()
        return None

    def fillHand(self,card):
        self.hand.append(card)
        return self

    def getHand(self):
        return self.hand

