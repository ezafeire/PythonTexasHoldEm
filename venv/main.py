import player,deck,card

class Main(object):

    players = list()
    deck = list()
    def createPlayers(self,numberOfPlayers):
        for x in range(numberOfPlayers):
            self.players.append(player.Player(5000))
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

#separate game in rounds, loop back to every round until end of all action then proceed to next round!
game = Main().createPlayers(7).shuffle().giveCards()
#game.showAllPlayerCards()
print(game.deck.showEntireDeck())



