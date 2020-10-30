class Pawn():
    def __init__(self):
        self.pos = 0
        self.status = False
        self.safe_places = [5,11,16,21,27,32,37,43,48,53,59,64]
    
    def setPos(self, new_pos):
        """
        Will set the position of the pawn in the board
        """
        if new_pos <= 68:
            self.pos = new_pos
            self.isSafe()
    
    def getPos(self):
        return self.pos
    
    def setStatus(self):
        for spots in self.safe_places:
            if self.pos == spots:
                self.status = True
            else:
                self.status = False
    
    def Advance(self, new_pos):
        if new_pos <= 12:
            self.pos += new_pos
            self.isSafe()

    
    def isSafe(self):
        for spots in self.safe_places:
            if self.pos == spots:
                return True
    
    

    

