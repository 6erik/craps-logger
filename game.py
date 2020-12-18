# Game class module
from roll import Roll

class Game:
    def __init__(self):
        self.array_rolls = []

    def add_roll(self, roll):
        if type(roll) is Roll:
            self.array_rolls.append(roll)

        else:
            raise TypeError("Object must be of type 'Roll'")

    def get_roll_num(self):
        return len(self.array_rolls)
        