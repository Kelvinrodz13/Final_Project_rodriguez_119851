from ChesiBoard import *
from Helper import *

from DrawBoard import *
from graphics import *


Game = Board()

win = GraphWin('Parcheesi',1300,900)
GraphicInterface(win)

turncount = 0
player_cicle = 0

player_titles = ["Player Red Turn", "Player Blue Turn", "Player Yellow Turn", "Player Green Turn", ]

for i in range(len(Game.getPlayerList())):
    Game.getPlayerList()[i].drawPawns(win)


while(Game.WhoWon() != True):

    showPlayerTurn = Text(Point(900,100), player_titles[player_cicle])
    showPlayerTurn.setSize(25)
    showPlayerTurn.setOutline(color_rgb(0,0,0))

    if(player_cicle == 0):
        showPlayerTurn.setTextColor('Red')
    elif(player_cicle == 1):
        showPlayerTurn.setTextColor('Blue')
    elif(player_cicle == 2):
        showPlayerTurn.setTextColor(color_rgb(199,193,11))
    else:
        showPlayerTurn.setTextColor('Green')
    

    showPlayerTurn.draw(win)



    currentPlayer = Game.getPlayer(player_cicle)
    PlayerTurnEvent(currentPlayer,Game,win)


    if player_cicle == 3:
        player_cicle = 0
    else:
        player_cicle += 1
    
    showPlayerTurn.undraw()
    

showPlayerTurn.undraw()
showPlayerTurn.setText('Player {} won the game!!!'.format(Game.getWhoWon()))
showPlayerTurn.draw(win)


win.getMouse()
win.close()