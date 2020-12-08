import tkinter as tk
import random

HEIGHT = 400
WIDTH = 400

# BACKEND LOGIC STUFF
class Die:
    def __init__(self):
        self.value = random.randrange(1,6)

    def getValue(self):
        return self.value

class Roll:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def getDie1value(self):
        return self.die1.getValue()
    
    def getDie2value(self):
        return self.die2.getValue()

    def getCombinedValue(self):
        return self.getDie1value() + self.getDie2value()

def rollDice():
    roll = Roll()
    array_game.append(roll)
    # print(array_game)


array_session = []
array_game = []


# GUI STUFF
root = tk.Tk()

frame = tk.Frame()
frame.pack()

btnRoll = tk.Button(frame, text="Button", command=rollDice)
btnRoll.pack()

root.mainloop()
