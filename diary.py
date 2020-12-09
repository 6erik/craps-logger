import tkinter as tk
from roll import Roll

# BACKEND LOGIC STUFF
def submit_dice():
    d1 = die1value.get()
    d2 = die2value.get()

    if (d1 > 0 and d2 > 0):
        console_out("You rolled " + str(d1) + " " + str(d2))
        roll = Roll(d1, d2)
        array_game.append(roll)

    else:
        console_out("Select dice values before submitting")

def console_out(text_string):
    text_console.insert(tk.INSERT,(text_string + "\n"))

array_session = []
array_game = []

game_in_progress = 0

while game_in_progress:
    print("in progres")








# GUI STUFF
root = tk.Tk()

frame_main = tk.Frame(root)
frame_main.pack()

menu_bar = tk.Menu(root)
menu_commands = tk.Menu(menu_bar, tearoff=0)
menu_commands.add_radiobutton(label="Start logging", command=start_game)
menu_commands.add_checkbutton(label="End logging", command=root.quit)
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

root.config(menu=menu_bar)
root.mainloop()
