# dice.py

from random import randrange

class Dice:
    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1,7)

    def rollAll(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]