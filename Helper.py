from ChesiBoard import *
from graphics import *

from graphical_functions.Diceview import *
def PlayerTurnEvent(player = User(), game = Board(), win = GraphWin):

    """
    Helper function that runs a turn for a specific user
    """


    Dice1,Dice2 = player.RollDice() # Dice roll result will be stored here

#_________________________________________________________________ Graphical sections

    title = Text(Point(900,50),"Welcome to Parcheesi")
    title.setSize(30)
    title.draw(win)

    title2 = Text(Point(900,200),"Click anywhere to roll the dice ")
    title2.setSize(25)
    title2.draw(win)

    win.getMouse()

    graphDices1 = DieView(win,Point(850,300),100)
    graphDices1.setValue(Dice1)

    graphDices2 = DieView(win,Point(950,300),100)
    graphDices1.setValue(Dice2)


    title2.undraw()

#_________________________________________________________________

    isDouble = False # boolean that determine if the player achieved a double in their roll

    if Dice1 == Dice2: # validate if user rolled a double
        isDouble = True

    Dice1_been_used = False # 2 boolean variables that determine used the rolls to already spawn a pawn or to move a pawn
    Dice2_been_used = False


    print("Dice Results: {} and {}".format(Dice1,Dice2)) # print dice results from the roll

    Main_Choice = 'null'
    textEntry = Entry(Point(900,590),1)
    textEntry.setSize(14)
    textEntry.setFill(color_rgb(167, 197, 253))

    while Main_Choice != 'c':

        Title3 = Text(Point(900,475),"Select a Action\na) Spawn a new pawn.\nb)Move a Pawn.\nc)End Turn.\n")
        Title3.setSize(18)
        Title3.draw(win)

        textEntry.draw(win)

        clickWord = Text(Point(900,550), 'Click anywhere to enter guess!')
        clickWord.draw(win)
        
        win.getMouse() #click function as enter
        clickWord.undraw()

        Main_Choice = textEntry.getText() 

        textEntry.undraw()


        if Main_Choice == 'a' and ((Dice1 == 5 or Dice2 == 5) or (Dice1+Dice2 == 5)):
            if Dice1 == 5 or Dice2 ==5: #Chech which of the dice contain a 5
                if Dice1 == 5:
                    for i in range(len(game.getPlayerList())):
                            temp = game.getPlayer(i)
                            if player.isBlocked(temp,i) == False:
                                player.leaveNest(player.getColor()) # spawn a new pawn of the player
                                Dice1_been_used = True
                            else:
                                print("Pawn cannot leave nest. Opposing player is blocking spawn point.",'\n')
                else:
                    for i in range(len(game.getPlayerList())):
                            temp = game.getPlayer(i)
                            if player.isBlocked(temp,i) == False:
                                player.leaveNest(player.getColor()) # spawn a new pawn of the player
                                Dice2_been_used = True
                            else:
                                print("Pawn cannot leave nest. Opposing player is blocking spawn point.",'\n')
            else:
                if (Dice1+Dice2) == 5: #Check if the sum of both dices actually equals 5
                    for i in range(len(game.getPlayerList())):
                            temp = game.getPlayer(i)
                            if player.isBlocked(temp,i) == False:
                                player.leaveNest(player.getColor()) # spawn a new pawn of the player
                                Dice1_been_used = True
                                Dice2_been_used = True
                            else:
                                print("Pawn cannot leave nest. Opposing player is blocking spawn point.",'\n')
                    
        else:
            if Main_Choice == 'b':
                if player.PawnsInField() != 0: # validate if the user has a pawn in the field to move
                    print("Which pawn do you wish to move? ")

                    for i in range(4):
                        if player.getPawn(i).getPos() > 0:
                            print("{}st Pawn located in {}".format(i+1,player.getPawn(i).getPos()))
                    
                    chosenPawn = int(input("Choose pawn you wish to move by location: ")) # chosen pawn to be moved
                    chosenValue = int(input("Pick which value to the pawn? Value1: {} or Value2{} or Value3: {}: ".format(Dice1, Dice2, Dice1+Dice2))) # chosen value to be used to move the pawn


                    if chosenValue  == 1 and Dice1_been_used != True: #Check if the Dice1 Value has been used already 
                        player.getPawn(chosenPawn-1).Advance(Dice1)
                        
                        for i in range(len(game.getPlayerList())):
                            temp = game.getPlayer(i)
                            player.Devour(temp) # verify if the pawn landed in another players spot, to be devoured and sent to the nest

                        player.Pawn_Reach_End() #validate if the user reached the end of color path
                        Dice1_been_used = True
                        print("Pawn has moved {} steps".format(Dice1))
                    else:
                        if chosenValue  == 2 and Dice2_been_used != True: #Check if the Dice2 Value has been used already 
                            player.getPawn(chosenPawn-1).Advance(Dice2)
                            player.Devour()
                            player.Pawn_Reach_End() #validate if the user reached the end of color path
                            Dice2_been_used = True
                            print("Pawn has moved {} steps".format(Dice2))
                        else:
                            if chosenValue  == 3 and (Dice1_been_used != True and Dice2_been_used != True): #Check if the Dice1 adn Dice2 Value has been used already 
                                player.getPawn(chosenPawn-1).Advance(Dice2 + Dice2)
                                player.Pawn_Reach_End()#validate if the user reached the end of color path
                                Dice2_been_used = True
                                print("Pawn has moved {} steps".format(Dice2+Dice1))
                            else:
                                print("Dice values have been used, please end turn.\n")  #Error message went both dice values have been used
    
    Title3.undraw()
    title.undraw()
    
    player.Pawn_Reach_End()

    if isDouble == True :
        PlayerTurnEvent(player,game,win)


