# Roll class module

class Roll:
    def __init__(self, die1, die2):
        self.die1 = die1
        self.die2 = die2

    def getDie1value(self):
        return self.die1.getValue()
    
    def getDie2value(self):
        return self.die2.getValue()

    def getCombinedValue(self):
        return self.getDie1value() + self.getDie2value()