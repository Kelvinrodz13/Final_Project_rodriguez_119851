class Pawn():
    def __init__(self):
        """
        class constructor
        pos - tracks the pawns position
        safe_places = tracks are of the board where pawns cannot be devoured
        """
        self.pos = 0
        self.status = False
        self.safe_places = [5,12,17,22,29,34,39,46,56,63,68]
        self.amount_steps_taken = 0
    
    def setPos(self, new_pos):
        """
        Will set the position of the pawn in the board
        """
        if new_pos <= 68:
            self.pos = new_pos
            self.isSafe()
    
    def getStepsTaken(self):
        return self.amount_steps_taken
    
    def getPos(self):
        """
        return postion of a pawn
        """
        return self.pos
    
    def setStatus(self):
        """
        function that sets the status of pawn if their are safe(true) or unsafe(false)
        """
        for spots in self.safe_places:
            if self.pos == spots:
                self.status = True
            else:
                self.status = False
    
    def Advance(self, new_pos):
        """
        function that advances the pawn throught the board
        """
        if new_pos <= 12:
            self.pos += new_pos
            self.amount_steps_taken += new_pos
            self.isSafe()

    
    def isSafe(self):
        """
        validate if the pawn is found in safe spot
        """
        for spots in self.safe_places:
            if self.pos == spots:
                return True
    
    

    

