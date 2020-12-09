# Roll class module

class Roll:
    def __init__(self, die1, die2):
        self.die1 = die1
        self.die2 = die2

    def get_die1_value(self):
        return self.die1
    
    def get_die2_value(self):
        return self.die2

    def get_dice_total(self):
        return self.get_die1_value() + self.get_die2_value()