import random
from Helper import *

class BotNumTwo:
    def __init__(self):
        self.GameBoard = Empty
        self.Char = Empty
        self.Opponent = Empty

    def play(self, GameBoard, Char):
        # reinitialize the current turn properties
        self.GameBoard = GameBoard
        self.Char = Char
        self.Opponent = GetOpponent(Char)
        AvailableMoves = GetAvailableMoves(GameBoard)

        return random.randint(0, 8)
