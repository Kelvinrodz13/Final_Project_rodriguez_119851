from Pawn import *
import random
class User():
    def __init__(self,new_name=str):
        self.color = new_name
        self.PawnList = [Pawn(),Pawn(),Pawn(),Pawn()]
        self.PiecesAtEnd = 0
    
    def setColor(self, newColor=str):
        self.color = newColor
    
    def getColor(self):
        return self.color
    
    def getPawn(self,index=int):
        return self.PawnList[index]
    
    def PawnsInField(self):
        amount = 0
        for i in range(len(self.PawnList)):
            if self.PawnList[i].getPos() != 0:
                amount += 1

        return amount
    
    def leaveNest(self,color = str):
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
        return random.randint(1,6) , random.randint(1,6)
    
    def Devour(self, adversary, pos=int):
        for pawns in self.PawnList:
            for adv_pawns in adversary.PawnList:
                if pawns.getPos() == adv_pawns.getPos():
                    adv_pawns.setPos(0)
                    adv_pawns.setStatus(True)
                else:
                    continue
    

