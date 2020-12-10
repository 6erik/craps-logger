import tkinter as tk
import tkinter.scrolledtext as st
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
    global r1_pass_win, r1_dont_win, after_pass_win, after_dont_win
    global strvar_r1pw, strvar_r1dw, strvar_apw, strvar_adw

    game_number += 1

    if roll_number == 1:
        if val == 7 or val == 11:
            console_out("Pass WIN - Dont LOSS")
            r1_pass_win += 1
            strvar_r1pw.set(str(r1_pass_win))
        
        elif val == 2 or val == 3:
            console_out("Pass LOSS - Dont WIN")
            r1_dont_win += 1
            strvar_r1dw.set(str(r1_dont_win))
        
        else: # if val is 12
            console_out("Pass LOSS - Dont PUSH")

    else:
        if val == 7:
            console_out("Pass LOSS - Dont WIN")
            after_dont_win += 1
            strvar_adw.set(str(after_dont_win))
        else:
            console_out("Pass WIN - Dont LOSS")
            after_pass_win += 1
            strvar_apw.set(str(after_pass_win))
    
    roll_number = 0
    array_session.append(array_game)
    array_game.clear()

def console_out(text_string):
    text_console.insert(tk.END, (text_string + "\n"))
    text_console.see(tk.END)

# GUI CODE CONTINUED
frame_main = tk.Frame(root)
frame_main.pack()

### MENU - commands
menu_bar = tk.Menu(root)
menu_commands = tk.Menu(menu_bar, tearoff=0)
menu_commands.add_command(label="Start logging", command=start_game)
menu_commands.add_separator()
menu_commands.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="Commands", menu=menu_commands)

### FRAME - dice select
### TK VARS
die1value = tk.IntVar()
die2value = tk.IntVar()

frame_dice_select = tk.Frame(frame_main)
frame_dice_select.grid(row=0, column=0)

## SUBFRAME - die1 & die2
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

### FRAME - statistics
### TK VARS
strvar_r1pw = tk.StringVar()
strvar_r1dw = tk.StringVar()
strvar_apw = tk.StringVar()
strvar_adw = tk.StringVar()

frame_statistics = tk.Frame(frame_main)
frame_statistics.grid(row=0, column=1)

label_statistics = tk.Label(frame_statistics, text="Statistics")
label_statistics.grid(row=0, column=1)

label_pass = tk.Label(frame_statistics, text="Pass")
label_pass.grid(row=1, column=1)

label_dontpass = tk.Label(frame_statistics, text="Don't")
label_dontpass.grid(row=1, column=2)

label_first = tk.Label(frame_statistics, text="R1", anchor="w")
label_first.grid(row=2, column=0)

label_rest = tk.Label(frame_statistics, text="R2+", anchor="w")
label_rest.grid(row=3, column=0)

label_r1_pass_win = tk.Label(frame_statistics, textvariable=strvar_r1pw)
label_r1_pass_win.grid(row=2, column=1)

label_r1_dont_win = tk.Label(frame_statistics, textvariable=strvar_r1dw)
label_r1_dont_win.grid(row=2, column=2)

label_after_pass_win = tk.Label(frame_statistics, textvariable=strvar_apw)
label_after_pass_win.grid(row=3, column=1)

label_after_dont_win = tk.Label(frame_statistics, textvariable=strvar_adw)
label_after_dont_win.grid(row=3, column=2)

### FRAME - console
frame_console = tk.Frame(frame_main)
frame_console.grid(row=1)

text_console = st.ScrolledText(frame_console)
text_console.pack()

# ARRAYS FOR FULL SESSION AND GAME LOGS
array_session = []
array_game = []

# PER SESSION VARIABLES
session_in_progress = 0
game_number = 0

r1_pass_win = 0
r1_dont_win = 0
after_pass_win = 0
after_dont_win = 0

# PER GAME VARIABLES
point = 0
roll_number = 0

root.config(menu=menu_bar)
root.mainloop()
