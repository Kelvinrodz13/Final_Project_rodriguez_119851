def PlayerTurnEvent(player = User(), game = Board()):
    Dice_Result = []
    Dice1,Dice2 = player.RollDice()

    Dice1_been_used = False
    Dice2_been_used = False


    Dice_Result.append(Dice1)
    Dice_Result.append(Dice2)

    print("Dice Results: {} and {}".format(Dice1,Dice2))

    Main_Choice = 'null'

    while Main_Choice != 'c':
        Main_Choice = str(input("Select a Action\na) Spawn a new pawn.\nb)Move a Pawn.\nc)End Turn.\n"))

        if Main_Choice == 'a' and ((Dice1 == 5 or Dice2 == 5) or (Dice1+Dice2 == 5)):
            if Dice1 == 5 or Dice2 ==5:
                if Dice1 == 5:
                    player.leaveNest(player.getColor())
                    Dice1_been_used = True
                else:
                    player.leaveNest(player.getColor())
                    Dice2_been_used = True
            else:
                if (Dice1+Dice2) == 5:
                    player.leaveNest(player.getColor())
                    Dice1_been_used = True
                    Dice2_been_used = True
        else:
            if Main_Choice == 'b':
                if player.PawnsInField() != 0:
                    print("Which pawn do you wish to move? ")

                    for i in range(4):
                        if player.getPawn(i).getPos() > 0:
                            print("{}st Pawn located in {}".format(i+1,player.getPawn(i).getPos()))
                    
                    chosenPawn = int(input("Choose pawn you wish to move by location: "))
                    chosenValue = int(input("Pick which value to the pawn? Value1: {} or Value2{} or Value3: {}: ".format(Dice1, Dice2, Dice1+Dice2)))


                    if chosenValue  == 1 and Dice1_been_used != True:
                        player.getPawn(chosenPawn-1).Advance(Dice1)
                        Dice1_been_used = True
                        print("Pawn has moved {} steps".format(Dice1))
                    else:
                        if chosenValue  == 2 and Dice2_been_used != True:
                            player.getPawn(chosenPawn-1).Advance(Dice2)
                            Dice2_been_used = True
                            print("Pawn has moved {} steps".format(Dice2))
                        else:
                            if chosenValue  == 3 and (Dice1_been_used != True and Dice2_been_used != True):
                                player.getPawn(chosenPawn-1).Advance(Dice2 + Dice2)
                                Dice2_been_used = True
                                print("Pawn has moved {} steps".format(Dice2+Dice1))
                            else:
                                print("Dice values have been used, please end turn.\n")
