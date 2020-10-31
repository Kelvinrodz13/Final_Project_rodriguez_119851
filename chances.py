from graphics import *
import random
import shuffle

dice = [1,2,3,4,5,6]
Dice = random.choice(dice)

def chance(self,win):
        while True:
            win.getMouse()
            Dice = random.choice(dice)
            if Dice == 1:
                shuffle.get1()
            if Dice == 2:
                shuffle.get2()
            if Dice == 3:
                shuffle.get3()
            if Dice == 4:
                shuffle.get4()
            if Dice == 5:
                shuffle.get5()
            if Dice == 6:
                shuffle.get6()
            win.getMouse()
            shuffle.reset()
            Dice = random.choice(dice)