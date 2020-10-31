from ChesiBoard import *
from Helper import *

from graphical_functions.DrawBoard import *
from graphics import *


Game = Board()

win = GraphWin('Parcheesi',1200,800)
GraphicInterface(win)

turncount = 0
player_cicle = 0

player_titles = ["Player Yellow Turn", "Player Blue Turn", "Player Red Turn", "Player Green Turn", ]



while(Game.WhoWon() != True):

    showPlayerTurn = Text(Point(900,100), player_titles[player_cicle])
    showPlayerTurn.setSize(25)
    showPlayerTurn.setOutline(color_rgb(0,0,0))

    if(player_cicle == 0):
        showPlayerTurn.setTextColor(color_rgb(199,193,11))
    elif(player_cicle == 1):
        showPlayerTurn.setTextColor('Blue')
    elif(player_cicle == 2):
        showPlayerTurn.setTextColor('Red')
    else:
        showPlayerTurn.setTextColor('Green')
    

    showPlayerTurn.draw(win)


    currentPlayer = Game.getPlayer(player_cicle)
    PlayerTurnEvent(currentPlayer,Game,win)


    if player_cicle == 4:
        player_cicle = 0
    else:
        player_cicle += 1
    
    showPlayerTurn.undraw()
    


print('Player {} won the game!!!'.format(Game.getWhoWon()))


win.getMouse()
win.close()