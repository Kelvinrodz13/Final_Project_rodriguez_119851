from User import *

class Board():
    def __init__(self):
        self.players = [User('Red'),User('Blue'),User('Yellow'),User('Green')]
    
    def getPlayer(self, index=int):
        return self.players.__getitem__(index)
    
    def WhoWon(self):
        for person in self.players:
            if person.PiecesAtEnd() == 4:
                return True
        
        return False

    def getWhoWon(self):
        for person in self.players:
            if person.PiecesAtEnd() == 4:
                return person.getColor()

    


