import tkinter as tk

HEIGHT = 400
WIDTH = 400

# BACKEND LOGIC STUFF
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

def submitDice():
    d1 = die1value.get()
    d2 = die2value.get()

    if (d1 > 0 and d2 > 0):
        consoleOut("You rolled " + str(d1) + " " + str(d2))
        roll = Roll(d1, d2)
        array_game.append(roll)

    else:
        consoleOut("Select dice values before submitting")

def consoleOut(text_string):
    text_console.insert(tk.INSERT,(text_string + "\n"))


array_session = []
array_game = []

# GUI STUFF
root = tk.Tk()

frame_main = tk.Frame()
frame_main.pack()

frame_dice_select = tk.Frame(frame_main)
frame_dice_select.pack()

frame_die1 = tk.Frame(frame_dice_select)
frame_die1.grid(row=0, column=0)
frame_die2 = tk.Frame(frame_dice_select)
frame_die2.grid(row=0, column=1)
frame_submit = tk.Frame(frame_dice_select)
frame_submit.grid(row=0, column=2)

die1value = tk.IntVar()
die2value = tk.IntVar()

d1r1 = tk.Radiobutton(frame_die1, text="1", variable=die1value, value=1)
d1r1.pack()
d1r2 = tk.Radiobutton(frame_die1, text="2", variable=die1value, value=2)
d1r2.pack()
d1r3 = tk.Radiobutton(frame_die1, text="3", variable=die1value, value=3)
d1r3.pack()
d1r4 = tk.Radiobutton(frame_die1, text="4", variable=die1value, value=4)
d1r4.pack()
d1r5 = tk.Radiobutton(frame_die1, text="5", variable=die1value, value=5)
d1r5.pack()
d1r6 = tk.Radiobutton(frame_die1, text="6", variable=die1value, value=6)
d1r6.pack()

d2r1 = tk.Radiobutton(frame_die2, text="1", variable=die2value, value=1)
d2r1.pack()
d2r2 = tk.Radiobutton(frame_die2, text="2", variable=die2value, value=2)
d2r2.pack()
d2r3 = tk.Radiobutton(frame_die2, text="3", variable=die2value, value=3)
d2r3.pack()
d2r4 = tk.Radiobutton(frame_die2, text="4", variable=die2value, value=4)
d2r4.pack()
d2r5 = tk.Radiobutton(frame_die2, text="5", variable=die2value, value=5)
d2r5.pack()
d2r6 = tk.Radiobutton(frame_die2, text="6", variable=die2value, value=6)
d2r6.pack()

button_submit = tk.Button(frame_submit, text="Submit", command=submitDice)
button_submit.pack()

frame_console = tk.Frame(frame_main)
frame_console.pack()

text_console = tk.Text(frame_console)
text_console.pack()

root.mainloop()
