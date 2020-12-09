import tkinter as tk
from roll import Roll

# GUI CODE
root = tk.Tk()
root.title("Craps Logger")

# MODULE DEFINITIONS
def submit_dice():
    global session_in_progress, roll_number, game_number

    d1 = die1value.get()
    d2 = die2value.get()

    if session_in_progress:
        if (d1 > 0 and d2 > 0):
            console_out("Gm"+ str(game_number+1) + "-Rd" + str(roll_number+1) + ": " + str(d1) + " " + str(d2))
            roll = Roll(d1, d2)
            array_game.append(roll)
            print("Roll(" + str(d1) + "," + str(d2) + ")")
            roll_number += 1
            make_game_decision()

        else:
            console_out("Select dice values before submitting")

    else:
        console_out("Start game logging before submitting dice values")

def start_game():
    global session_in_progress
    session_in_progress = 1
    print("Logging started")

def make_game_decision():
    global array_game, point, roll_number, game_number
    val = array_game[roll_number - 1].get_dice_total()

    if roll_number == 1: # if point has not been set
        if (val == 4 or val == 5 or val == 6 or val == 8 or val == 9 or val == 10):
            point = val
            game_number += 1
            console_out("The point is: " + str(val))
        else:
            game_over(val)
    
    else:
        if val == point:
            game_over(val)
        elif val == 7:
            game_over(val)
        else:
            pass

def game_over(val):
    global session_in_progress, point, roll_number, game_number, array_session, array_game
    game_number += 1

    if roll_number == 1:
        if val == 7 or val == 11:
            console_out("Passline win!")
        
        elif val == 2 or val == 3:
            console_out("Passline loss.")
        
        else:
            console_out("Passline loss.")

    else:
        if val == 7:
            console_out("Passline loss.")
        else:
            console_out("Passline win!")
    
    roll_number = 0
    array_session.append(array_game)
    array_game.clear()

def console_out(text_string):
    text_console.insert(tk.INSERT,(text_string + "\n"))

# GUI CODE CONTINUED
frame_main = tk.Frame(root)
frame_main.pack()

menu_bar = tk.Menu(root)
menu_commands = tk.Menu(menu_bar, tearoff=0)
menu_commands.add_command(label="Start logging", command=start_game)
menu_commands.add_command(label="End logging", command=root.quit)
menu_commands.add_separator()
menu_commands.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="Commands", menu=menu_commands)


frame_dice_select = tk.Frame(frame_main)
frame_dice_select.pack()

frame_die1 = tk.Frame(frame_dice_select)
frame_die1.grid(row=0, column=1)
frame_die2 = tk.Frame(frame_dice_select)
frame_die2.grid(row=1, column=1)
frame_submit = tk.Frame(frame_dice_select)
frame_submit.grid(row=2, column=1)

label_die1 = tk.Label(frame_dice_select, text="Die 1: ")
label_die1.grid(row=0, column=0)
label_die2 = tk.Label(frame_dice_select, text="Die 2: ")
label_die2.grid(row=1, column=0)

die1value = tk.IntVar()
die2value = tk.IntVar()

d1r1 = tk.Radiobutton(frame_die1, text="1", variable=die1value, value=1)
d1r1.grid(row=0, column=0)
d1r2 = tk.Radiobutton(frame_die1, text="2", variable=die1value, value=2)
d1r2.grid(row=0, column=1)
d1r3 = tk.Radiobutton(frame_die1, text="3", variable=die1value, value=3)
d1r3.grid(row=0, column=2)
d1r4 = tk.Radiobutton(frame_die1, text="4", variable=die1value, value=4)
d1r4.grid(row=0, column=3)
d1r5 = tk.Radiobutton(frame_die1, text="5", variable=die1value, value=5)
d1r5.grid(row=0, column=4)
d1r6 = tk.Radiobutton(frame_die1, text="6", variable=die1value, value=6)
d1r6.grid(row=0, column=5)

d2r1 = tk.Radiobutton(frame_die2, text="1", variable=die2value, value=1)
d2r1.grid(row=0, column=0)
d2r2 = tk.Radiobutton(frame_die2, text="2", variable=die2value, value=2)
d2r2.grid(row=0, column=1)
d2r3 = tk.Radiobutton(frame_die2, text="3", variable=die2value, value=3)
d2r3.grid(row=0, column=2)
d2r4 = tk.Radiobutton(frame_die2, text="4", variable=die2value, value=4)
d2r4.grid(row=0, column=3)
d2r5 = tk.Radiobutton(frame_die2, text="5", variable=die2value, value=5)
d2r5.grid(row=0, column=4)
d2r6 = tk.Radiobutton(frame_die2, text="6", variable=die2value, value=6)
d2r6.grid(row=0, column=5)

button_submit = tk.Button(frame_submit, text="Submit", command=submit_dice)
button_submit.pack()

frame_console = tk.Frame(frame_main)
frame_console.pack()

text_console = tk.Text(frame_console)
text_console.pack()

# ARRAYS FOR FULL SESSION AND GAME LOGS
array_session = []
array_game = []

# PER SESSION VARIABLES
session_in_progress = 0
game_number = 0

# PER GAME VARIABLES
point = 0
roll_number = 0

root.config(menu=menu_bar)
root.mainloop()
