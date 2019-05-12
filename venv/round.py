import player
class Round(object):

    def __init__(self,player,roundNumber):
        self.player=player
        self.roundNumber=roundNumber
        return None

    def raiseBet(self,amount):
        pass

    def callBet(self):
        pass

    def fold(self):
        pass

    def allIn(self):
        pass