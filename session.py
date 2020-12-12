# Session class module
from game import Game

class Session:
    def __init__(self):
        self.array_games = []

    def add_game(self, game):
        if type(game) is Game:
            self.array_games.append(game)

        else:
            raise TypeError("Object must be of type 'Game'")
    
    def get_game_num(self):
        return len(self.array_games)