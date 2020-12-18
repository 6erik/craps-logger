# Session class module
from game import Game

class Session:
    def __init__(self):
        self.array_games = []

        # Variables to keep statistics
        self.round1_pass_wins = 0
        self.round1_dont_wins = 0
        self.round1_dont_push = 0

        self.after_pass_wins = 0
        self.after_dont_wins = 0

        self.count_val = [0] * 6
        self.count_sum = [0] * 11

    def add_game(self, game):
        if type(game) is Game:
            self.array_games.append(game)

        else:
            raise TypeError("Object must be of type 'Game'")

    def process_roll(self, roll):
        #print(roll.get_dice_total() - 2)
        self.count_val[roll.get_die1_value() - 1] += 1
        self.count_val[roll.get_die2_value() - 1] += 1
        self.count_sum[roll.get_dice_total() - 2] += 1
    
    def get_game_num(self):
        return len(self.array_games)

    def get_round1_pass_wins(self):
        return self.round1_pass_wins

    def get_round1_dont_wins(self):
        return self.round1_dont_wins

    def get_after_pass_wins(self):
        return self.after_pass_wins

    def get_after_dont_wins(self):
        return self.after_dont_wins

    def get_count_val(self, value):
        return self.count_val[value - 1]

    def get_count_sum(self, sum):
        return self.count_sum[sum - 2]

    def set_winner(self, winner, roll_number):
        if winner == "pass":
            if roll_number > 1:
                self.after_pass_wins += 1
            
            else:
                self.round1_pass_wins += 1

        elif winner == "dont":
            if roll_number > 1:
                self.after_dont_wins += 1
            
            else:
                self.round1_dont_wins += 1
        
        else:
            pass
