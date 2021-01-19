import random
from Helper import *

class BotNumOne:
    def __init__(self):
        self.GameBoard = None
        self.Char = None
        self.Opponent = None
        self.GameEnded = False

    def play(self, GameBoard, Char):
        # reinitialize this turn properties
        self.GameBoard = GameBoard
        self.Char = Char
        self.Opponent = GetOpponent(Char)
        Least = -2
        BestPlay = []
        # the best position to start tic-tac-toe game is it's center
        if len(GetAvailableMoves(self.GameBoard)) is 9:
            return 4
        for Move in GetAvailableMoves(self.GameBoard):
            self.PlaceMark(Move, Char)
            Value = self.BestMove(GetOpponent(Char), -2, 2)
            self.PlaceMark(Move, None)
            if Value > Least:
                Least = Value
                BestPlay = [Move]
            elif Value == Least:
                BestPlay.append(Move)
        return random.choice(BestPlay)

    def Winner(self):
        for Char in ('X', 'O'):
            Moves = [Move for Move, Value in enumerate(self.GameBoard) if Value == Char]
            for WinningState in WinningStates:
                winner = True
                for Move in WinningState:
                    if Move not in Moves:
                        winner = False
                if winner:
                    if Char is self.Char:
                        self.GameEnded = True
                        return self.Char
                    elif Char is self.Opponent:
                        self.GameEnded = True
                        return self.Opponent
        Items = len([Item for Item, Value in enumerate(self.GameBoard) if Value is not None])
        if Items is 9 and self.Winner is None:
            self.GameEnded = True
            return 'Draw'
        return None


    def PlaceMark(self, Position, Mark):
        self.GameBoard[Position] = Mark

    # this algorithm use minimax algorithm with alpha beta pruning
    def BestMove(self, Char, Alpha, Beta):
        winner = self.Winner()
        if not self.GameEnded:
            if winner is self.Char:
                return 1
            elif winner is self.Opponent:
                return -1
            elif winner is 'Draw':
                return 0
        for Move in GetAvailableMoves(self.GameBoard):
            self.PlaceMark(Move, Char)
            Value = self.BestMove(GetOpponent(Char), Alpha, Beta)
            self.PlaceMark(Move, None)
            if Char == self.Char:
                if Value > Alpha:
                    Alpha = Value
                if Alpha >= Beta:
                    return Beta
            else:
                if Value < Beta:
                    Beta = Value
                if Beta <= Alpha:
                    return Alpha
        if Char == self.Char:
            return Alpha
        else:
            return Beta
