from User import *

class Board():
    def __init__(self):
        self.players = [User('Red'),User('Blue'),User('Yellow'),User('Green')]
    
    def __getitem__(self,index = 0):
        return self.players[index] 
    
    def getPlayer(self, index=int):
        return self.__getitem__(index)

    def getPlayerList(self):
        return self.players
    
    def WhoWon(self):
        for person in self.players:
            if person.getPiecesAtEnd() == 4:
                return True
        
        return False

    def getWhoWon(self):
        for person in self.players:
            if person.PiecesAtEnd() == 4:
                return person.getColor()

    


