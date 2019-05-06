import random

class Card(object):

    suitNames = {1: "S", 2: "H", 3: "C", 4: "D"}
    rankNames = {1: "A",2: "2",3: "3",4: "4",5: "5",6: "6",7: "7",8: "8",9: "9",10: "10",11: "J",12: "Q",13: "K"}

    def __init__(self,rank,suit):
        self.suit= self.suitNames[suit]
        self.number = rank
        return None

    def getNumber(self):
        return self.number

    def getSuit(self):
        return self.suit

    def getBoth(self):
        return self.number,self.suit


