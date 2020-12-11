# Game class module
from roll import Roll

class Game:
    def __init__(self):
        self.array_rolls = []
        #self.array_die_count = [0] * 6
        #self.array_sum_count = [0] * 11

    def add_roll(self, roll):
        if type(roll) is Roll:
            #self.array_die_count[roll.get_die1_value() -1] += 1
            #self.array_die_count[roll.get_die2_value() -1] += 1
            #self.array_sum_count[roll.get_dice_total() -1] += 1
            self.array_rolls.append(roll)

        else:
            raise TypeError("Object must be of type 'Roll'")

    #def get_die_count(self, die_value):
        #return self.array_die_count[die_value - 1]

    #def get_sum_count(self, sum_value):
        #return self.array_sum_count[sum_value - 1]