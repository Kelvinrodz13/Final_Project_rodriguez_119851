def PlayerTurnEvent(player = User(), game = Board()):
    """
    Helper function that runs a turn for a specific user
    """
    Dice1,Dice2 = player.RollDice() # Dice roll result will be stored here

    isDouble = False # boolean that determine if the player achieved a double in their roll

    if Dice1 == Dice2: # validate if user rolled a double
        isDouble = True

    Dice1_been_used = False # 2 boolean variables that determine used the rolls to already spawn a pawn or to move a pawn
    Dice2_been_used = False


    print("Dice Results: {} and {}".format(Dice1,Dice2)) # print dice results from the roll

    Main_Choice = 'null'

    while Main_Choice != 'c':
        Main_Choice = str(input("Select a Action\na) Spawn a new pawn.\nb)Move a Pawn.\nc)End Turn.\n")) # options player may choose from for their turn

        if Main_Choice == 'a' and ((Dice1 == 5 or Dice2 == 5) or (Dice1+Dice2 == 5)):
            if Dice1 == 5 or Dice2 ==5: #Chech which of the dice contain a 5
                if Dice1 == 5:
                    player.leaveNest(player.getColor()) # spawn a new pawn of the player
                    Dice1_been_used = True
                else:
                    player.leaveNest(player.getColor()) # spawn a new pawn for the player
                    Dice2_been_used = True
            else:
                if (Dice1+Dice2) == 5: #Check if the sum of both dices actually equals 5
                    player.leaveNest(player.getColor()) # spawn a new pawn for the player
                    Dice1_been_used = True
                    Dice2_been_used = True
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
                        Dice1_been_used = True
                        print("Pawn has moved {} steps".format(Dice1))
                    else:
                        if chosenValue  == 2 and Dice2_been_used != True: #Check if the Dice2 Value has been used already 
                            player.getPawn(chosenPawn-1).Advance(Dice2)
                            Dice2_been_used = True
                            print("Pawn has moved {} steps".format(Dice2))
                        else:
                            if chosenValue  == 3 and (Dice1_been_used != True and Dice2_been_used != True): #Check if the Dice1 adn Dice2 Value has been used already 
                                player.getPawn(chosenPawn-1).Advance(Dice2 + Dice2)
                                Dice2_been_used = True
                                print("Pawn has moved {} steps".format(Dice2+Dice1))
                            else:
                                print("Dice values have been used, please end turn.\n")  #Error message went both dice values have been used
    
    if(isDouble == True):
        PlayerTurnEvent(player,game)


