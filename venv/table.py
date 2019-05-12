import player,deck,card

class Table(object):

    def __init__(self, bigBlind):
        self.bigBlind=int(bigBlind)
        self.smallBlind=int(self.bigBlind/2)
        self.players=list()
        self.deck=list()
        self.pot=0
        self.tableId=0 # Should probably make a global counter somehow with table IDs so we can keep logs
        self.deck = deck.Deck() #already shuffled
        return None

    def createPlayer(self,name,cash):
        self.players.append(player.Player(name,cash))
        return self

    def shuffle(self):
        self.deck = deck.Deck()
        return self

    def getPlayers(self):
        return self.players

    def giveCards(self):
        for x in self.getPlayers():
            x.fillHand(self.deck.giveNextCard())
            x.fillHand(self.deck.giveNextCard())
        return self

    def showAllPlayerCards(self): #show all player hands for debugging only
        for x in self.getPlayers():
            print(x.getHand()[0].getBoth(),x.getHand()[1].getBoth())
        return self

    def assignBlinds(self):
        self.players[0].setBlind("SB").takeMoney(self.getSB())
        self.players[1].setBlind("BB").takeMoney(self.getBB())
        return self

    def getBB(self):
        return int(self.bigBlind)

    def getSB(self):
        return int(self.smallBlind)

    def getTableInfo(self):
        return self.tableId,self.getBB(),self.getSB()

    def takeBlindMoney(self):
        for x in players:
            if(x.getBlind()=="SB"):
                x.takeMoney(smallBlind)
            if(x.getBlind()=="BB"):
                x.takeMoney(bigBlind)
        return self



#separate game in rounds, loop back to every round until end of all action then proceed to next round!





