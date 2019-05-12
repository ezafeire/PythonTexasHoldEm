import card
class Player(object):

    blind=0

    def __init__(self,name,cash): #takes cash from player pocket
        self.cash=int(cash)
        self.name=name
        self.hand=list()
        return None

    def fillHand(self,card):
        self.hand.append(card)
        return self

    def getHand(self):
        return self.hand

    def setCash(self,cash):
        self.cash = cash #take from pocket
        return self

    def setBlind(self,blind):
        self.blind = blind
        return self

    def getBlind(self):
        return self.blind

    def takeMoney(self,amount):
        self.cash-= amount
        return self

    def addMoney(self, amount): #need to take from player's pocket and add to table money
        self.cash +=amount
        return self

    def getMoney(self):
        return self.cash

    def getName(self):
        return self.name

    def getPlayerInfo(self):
        return self.getName(),self.getMoney(),self.getBlind()