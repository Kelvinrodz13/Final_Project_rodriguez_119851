from Pawn import *
from graphics import *
import random

circleSize = 8


class User():
    def __init__(self, new_name=str):
        """
        color- color of the player on the board
        pwanList - list that store the total amount of pawns
        PiecesAtEnd = counts the amount of pawns at the final spot
        """
        self.color = new_name
        self.PawnList = [Pawn(), Pawn(), Pawn(), Pawn()]
        self.PiecesAtEnd = 0

    def getPiecesAtEnd(self):
        return self.PiecesAtEnd

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

    def getPawn(self, index=int):
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

    def leaveNest(self, color=str):
        """
        function that spawns the players spawn in their initial starting points.
        Each player have a different starting point depending on the color.
        """
        for i in range(len(self.PawnList)):
            if self.PawnList[i].getPos() == 0:
                if self.getColor() == 'Red':

                    self.PawnList[i].setPos(39)

                elif self.getColor() == 'Blue':

                    self.PawnList[i].setPos(22)

                elif self.getColor() == 'Yellow':

                    self.PawnList[i].setPos(5)

                else:

                    self.PawnList[i].setPos(56)

                return i
                break

    def Pawn_Reach_End(self):
        for i in range(len(self.PawnList)):
            if self.PawnList[i].getPos() == 68 and self.PawnList[i].getStepsTaken() == 63:
                self.PiecesAtEnd += 1
                self.PawnList.pop(i)

    def RollDice(self):
        """
        simulate the rolling of a dice and also returns the result of the dice roll
        """
        return random.randint(1, 6), random.randint(1, 6)

    def Devour(self, adversary = Pawn ,color = str, i = int):
        """
        if a player lands in the same spot as another user, an event will occur where the player will capture the spot and losing side's pawn
        will be captured and sent to nest.
        """
        eat =False
        for pawns in self.PawnList:
            if ( (pawns.pos == adversary.pos and self.getColor() != color) and (pawns.isSafe() != True and adversary.isSafe() != True) ):
                    adversary.amount_steps_taken = 0
                    adversary.setStatus()
                    eat = True
                    return eat
        
        return eat

    def isBlocked(self, adversary, pawnIndex=int):
        """ Check if the pawn is blocked from spawning"""
        for adv_pawns in adversary.PawnList:
            if(self.getColor() != adversary.getColor()) and (self.PawnList[pawnIndex].getPos() == adv_pawns.getPos()):
                return True

            return False

    def isBlocked(self, adversary):
        """ Overloaded function that check for blocked movement between all of adversarys pawn"""
        for pawns in self.PawnList:
            for adv_pawns in adversary.PawnList:
               if(self.getColor() != adversary.getColor()) and (pawns.getPos() == adv_pawns.getPos()):
                   return True

            return False
