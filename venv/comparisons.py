import card

class Comparisons(object):

    def __init__(self,cardsDown,hand):
        self.hand = hand
        self.cardsDown = cardsDown
        self.total = self.hand+self.cardsDown
        self.orderTotal()
        return None

    def orderTotal(self):
        self.total.sort(reverse=True)
        return self

    def compare(self, card1, card2):  # returns 1 if card1>card2
        if (card1.getNumber() > card2.getNumber()):
            return 1
        elif (card1.getNumber() < card2.getNumber()):
            return 0
        else:
            return -1

    #maybe something that returns a power value or the highest card in some? i.e straight returns highest number and it wins over lower number straight. flush returns nothing
    def isStraightFlush(self): pass
    def isQuads(self): pass
    def isFullHouse(self): pass
    def isFlush(self): pass
    def isStraight(self): pass
    def isThree(self): pass
    def isTwoPair(self): pass
    def isOnePair(self): pass
    def isHighCard(self): pass


comp = Comparisons([1,3,2,8,2],[2,10])
comp.orderTotal()
#print (comp.total)