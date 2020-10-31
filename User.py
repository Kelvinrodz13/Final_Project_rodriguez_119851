from Pawn import *
from graphics import *
from coordinates import *
import random

circleSize = 8
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

        if self.color == 'Red':
            self.graphPawns = [
            Circle(Point(100,100), circleSize),
            Circle(Point(118,100), circleSize),
            Circle(Point(128,100),circleSize),
            Circle(Point(138,100), circleSize)]

        elif self.color == 'Blue':
            self.graphPawns = [
            Circle(Point(440,107), circleSize),
            Circle(Point(450,107), circleSize),
            Circle(Point(460,107), circleSize),
            Circle(Point(470,107), circleSize)]
        elif self.color == 'Yellow':
            self.graphPawns = [
            Circle(Point(440,455), circleSize),
            Circle(Point(450,455), circleSize),
            Circle(Point(460,455), circleSize),
            Circle(Point(470,455), circleSize)]
        else:
            self.graphPawns = [
            Circle(Point(100,455), circleSize),
            Circle(Point(118,455), circleSize),
            Circle(Point(128,455), circleSize),
            Circle(Point(138,455), circleSize)]


    
    def getPiecesAtEnd(self):
        return self.PiecesAtEnd

    def moveGraph_Pawn(self, new_pos, index,win = GraphWin):
        temp = boardCoords[new_pos]
        self.graphPawns[index].undraw()
        self.graphPawns.insert(index,Circle(Point(temp.x,temp.y), circleSize))
        self.graphPawns[index].setFill(self.getColor())
        self.graphPawns[index].draw(win)

    
    def drawPawns(self,win = GraphWin):
        for i in range(len(self.graphPawns)):
            self.graphPawns[i].setFill(self.getColor())
            self.graphPawns[i].draw(win)
    
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
    
    def leaveNest(self,color = str,win = GraphWin):
        """
        function that spawns the players spawn in their initial starting points.
        Each player have a different starting point depending on the color.
        """
        for i in range(len(self.PawnList)):
            if self.PawnList[i].getPos() == 0:
                if self.getColor() == 'Red':

                    self.PawnList[i].setPos(39)
                    temp = boardCoords[39]

                    self.graphPawns[i].undraw()
                    self.graphPawns.insert(i,Circle(Point(temp.x,temp.y), circleSize))
                    self.graphPawns[i].setFill(self.getColor())
                    self.graphPawns[i].undraw()
                    self.graphPawns[i].draw(win)

                    

                elif self.getColor() == 'Blue':

                    self.PawnList[i].setPos(22)
                    temp = boardCoords[22]

                    self.graphPawns[i].undraw()
                    self.graphPawns.insert(i,Circle(Point(temp.x,temp.y), circleSize))
                    self.graphPawns[i].setFill(self.getColor())

                    self.graphPawns[i].undraw()
                    self.graphPawns[i].draw(win)
                    

                elif self.getColor() == 'Yellow':

                    self.PawnList[i].setPos(5)
                    temp = boardCoords[5]

                    self.graphPawns[i].undraw()
                    self.graphPawns.insert(i,Circle(Point(temp.x,temp.y), circleSize))
                    self.graphPawns[i].setFill(self.getColor())

                    self.graphPawns[i].undraw()
                    self.graphPawns[i].draw(win)
                    

                else:

                    self.PawnList[i].setPos(56)
                    temp = boardCoords[56]

                    self.graphPawns[i].undraw()
                    self.graphPawns.insert(i,Circle(Point(temp.x,temp.y), circleSize))
                    self.graphPawns[i].setFill(self.getColor())

                    self.graphPawns[i].undraw()
                    self.graphPawns[i].draw(win)
                
                return i
                break
    
    def returnGraph_Pawn_Start(self,i = int,win = GraphWin):

        if self.getColor() == 'Red':
            if i == 1:
                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(100,100),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
                
            elif i == 2:
                

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(118,100),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)

            elif i == 3:
                

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(128,100),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            else:
               
                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(138,100),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
                
        elif self.getColor() == 'Blue':

            if i == 1:
                

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(440,107),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
                
            elif i == 2:
                

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(450,107),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            elif i == 3:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(460,1079),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            else:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(470,107),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            
        elif self.getColor() == 'Yellow':
            if i == 1:
                
                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(440,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)

            elif i == 2:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(450,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            elif i == 3:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(460,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            else:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(470,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            
        else:
            if i == 1:
                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(100,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            elif i == 2:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(118,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            elif i == 3:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(128,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            else:

                self.graphPawns[i].undraw()
                self.graphPawns.index(i,Circle(Point(138,455),circleSize))
                self.graphPawns[i].setFill(self.getColor())
                self.graphPawns[i].draw(win)
            
        
    
    def Pawn_Reach_End(self):
        for i in range(len(self.PawnList)):
            if self.getColor() == 'Yellow':
                if self.PawnList[i].getPos() == 68 and self.PawnList[i].getStepsTaken() == 63:
                    self.PiecesAtEnd += 1
                    self.PawnList.pop(i)

                    self.graphPawns[i].undraw()
                    self.graphPawns.pop(i)


    def RollDice(self):
        """
        simulate the rolling of a dice and also returns the result of the dice roll
        """
        return random.randint(1,6) , random.randint(1,6)
    
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
                    

                    
        

    
    def isBlocked(self,adversary,pawnIndex = int):
        """ Check if the pawn is blocked from spawning"""
        for adv_pawns in adversary.PawnList:
            if(self.getColor() != adversary.getColor()) and (self.PawnList[pawnIndex].getPos() == adv_pawns.getPos()):
                return True
            
            return False
    
    def isBlocked(self,adversary):
        """ Overloaded function that check for blocked movement between all of adversarys pawn"""
        for pawns in self.PawnList:
            for adv_pawns in adversary.PawnList:
               if(self.getColor() != adversary.getColor()) and (pawns.getPos() == adv_pawns.getPos()):
                   return True
            
            return False
