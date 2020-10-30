from Pawn import *
import random
class User():
    def __init__(self,new_name=str):
        """
        color- color of the player on the board
        pwanList - list that store the total amount of pawns
        PiecesAtEnd = counts the amount of pawns at the final spot
        """
        self.color = new_name
        self.PawnList = [Pawn(),Pawn(),Pawn(),Pawn()]
        self.PiecesAtEnd = 0
    
    def setColor(self, newColor=str):
        """
        set the color name of the player
        """
        self.color = newColor
    
    def getColor(self):
        """
        returns the color of the player
        """
        return self.color
    
    def getPawn(self,index=int):
        """
        return the pawn stored in the list by its index
        """
        return self.PawnList[index]
    
    def PawnsInField(self):
        """
        boolean function that validate if the player has any pawn in board
        """
        amount = 0
        for i in range(len(self.PawnList)):
            if self.PawnList[i].getPos() != 0:
                amount += 1

        return amount
    
    def leaveNest(self,color = str):
        """
        function that spawns the players spawn in their initial starting points.
        Each player have a different starting point depending on the color.
        """
        for i in range(len(self.PawnList)):
            if self.PawnList[i].getPos() == 0:
                if self.getColor() == 'Red':
                    self.PawnList[i].setPos(5)
                elif self.getColor() == 'Blue':
                    self.PawnList[i].setPos(21)
                elif self.getColor() == 'Yellow':
                    self.PawnList[i].setPos(37)
                else:
                    self.PawnList[i].setPos(53)

                break
    

    def RollDice(self):
        """
        simulate the rolling of a dice and also returns the result of the dice roll
        """
        return random.randint(1,6) , random.randint(1,6)
    
    def Devour(self, adversary = User(), pos=int):
        """
        if a player lands in the same spot as another user, an event will occur where the player will capture the spot and losing side's pawn
        will be captured and sent to nest.
        """
        for pawns in self.PawnList:
            for adv_pawns in adversary.PawnList:
                if pawns.getPos() == adv_pawns.getPos():
                    adv_pawns.amount_steps_taken = 0
                    adv_pawns.setPos(0)
                    adv_pawns.setStatus(True)
                else:
                    continue
    
