# Roll class module

class Roll:
    def __init__(self, die1, die2):
        if type(die1) is int and type(die2) is int:
            if (1 <= die1 <= 6) and (1 <= die2 <= 6):
                self.die1 = die1
                self.die2 = die2

            else:
                raise ValueError("Values must be between 1 and 6 -- inclusive")
        
        else:
            raise TypeError("Values must be of type 'int'")

    def get_die1_value(self):
        return self.die1
    
    def get_die2_value(self):
        return self.die2

    def get_dice_total(self):
        return self.get_die1_value() + self.get_die2_value()