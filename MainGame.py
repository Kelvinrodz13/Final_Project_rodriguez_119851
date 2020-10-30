from ChesiBoard import *
from Helper import *


Game = Board()

turncount = 0
player_cicle = 0

while(Game.WhoWon() != True):

    currentPlayer = Game.getPlayer(player_cicle)
    PlayerTurnEvent(currentPlayer,Game)

    if player_cicle == 4:
        player_cicle = 0
    else:
        player_cicle += 1

print('Player {} won the game!!!'.format(Game.getWhoWon()))