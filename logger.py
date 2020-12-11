import tkinter as tk
import tkinter.scrolledtext as st
from roll import Roll
from game import Game
from session import Session

def main():
    app = App()
    app.root.mainloop()

class App:
    def __init__(self):
        self.session = Session()
        self.game = Game()
        self.root = tk.Tk()
        self.root.title("Craps Logger")
        
        ### TK VARS
        self.die1value = tk.IntVar()
        self.die2value = tk.IntVar()
        self.strvar_r1pw = tk.StringVar()
        self.strvar_r1dw = tk.StringVar()
        self.strvar_apw = tk.StringVar()
        self.strvar_adw = tk.StringVar()

        self.r1_pass_win = 0
        self.r1_dont_win = 0
        self.after_pass_win = 0
        self.after_dont_win = 0

        # Starting GUI event loop
        self.create_widgets()

    def create_widgets(self):
        # GUI CODE CONTINUED
        frame_main = tk.Frame(self.root)
        frame_main.pack()

        ### MENU - commands
        menu_bar = tk.Menu(self.root)
        menu_commands = tk.Menu(menu_bar, tearoff=0)
        menu_commands.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="Commands", menu=menu_commands)

        ### FRAME - dice select
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

        d1r1 = tk.Radiobutton(frame_die1, text="1", variable=self.die1value, value=1)
        d1r1.grid(row=0, column=0)
        d1r2 = tk.Radiobutton(frame_die1, text="2", variable=self.die1value, value=2)
        d1r2.grid(row=0, column=1)
        d1r3 = tk.Radiobutton(frame_die1, text="3", variable=self.die1value, value=3)
        d1r3.grid(row=0, column=2)
        d1r4 = tk.Radiobutton(frame_die1, text="4", variable=self.die1value, value=4)
        d1r4.grid(row=0, column=3)
        d1r5 = tk.Radiobutton(frame_die1, text="5", variable=self.die1value, value=5)
        d1r5.grid(row=0, column=4)
        d1r6 = tk.Radiobutton(frame_die1, text="6", variable=self.die1value, value=6)
        d1r6.grid(row=0, column=5)

        d2r1 = tk.Radiobutton(frame_die2, text="1", variable=self.die2value, value=1)
        d2r1.grid(row=0, column=0)
        d2r2 = tk.Radiobutton(frame_die2, text="2", variable=self.die2value, value=2)
        d2r2.grid(row=0, column=1)
        d2r3 = tk.Radiobutton(frame_die2, text="3", variable=self.die2value, value=3)
        d2r3.grid(row=0, column=2)
        d2r4 = tk.Radiobutton(frame_die2, text="4", variable=self.die2value, value=4)
        d2r4.grid(row=0, column=3)
        d2r5 = tk.Radiobutton(frame_die2, text="5", variable=self.die2value, value=5)
        d2r5.grid(row=0, column=4)
        d2r6 = tk.Radiobutton(frame_die2, text="6", variable=self.die2value, value=6)
        d2r6.grid(row=0, column=5)

        button_submit = tk.Button(frame_submit, text="Submit", command=lambda : self.submit_dice(self.die1value.get(), self.die2value.get()))
        button_submit.pack()

        ### FRAME - statistics
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

        self.label_r1_pass_win = tk.Label(frame_statistics, textvariable=self.strvar_r1pw)
        self.label_r1_pass_win.grid(row=2, column=1)

        self.label_r1_dont_win = tk.Label(frame_statistics, textvariable=self.strvar_r1dw)
        self.label_r1_dont_win.grid(row=2, column=2)

        self.label_after_pass_win = tk.Label(frame_statistics, textvariable=self.strvar_apw)
        self.label_after_pass_win.grid(row=3, column=1)

        self.label_after_dont_win = tk.Label(frame_statistics, textvariable=self.strvar_adw)
        self.label_after_dont_win.grid(row=3, column=2)

        ### FRAME - console
        self.frame_console = tk.Frame(frame_main)
        self.frame_console.grid(row=1)

        self.text_console = st.ScrolledText(self.frame_console)
        self.text_console.configure(state="disabled", font=("Arial", 9))
        self.text_console.pack()

    ### FUNCTION DEFINITIONS
    def submit_dice(self, d1, d2):
        roll_number = self.game.get_roll_num()
        game_number = self.session.get_game_num()

        if (d1 > 0 and d2 > 0):
            roll = Roll(d1, d2)
            self.game.add_roll(roll)

            self.console_out("Gm "+ str(game_number + 1) + "- Rd " + str(roll_number + 1) + ": " + str(d1) + " " + str(d2))
            self.make_game_decision(roll)

        else:
            self.console_out("Select dice values before submitting")

    def make_game_decision(self, roll):
        val = roll.get_dice_total()
        roll_number = self.game.get_roll_num()
        print("mgd: " + str(roll_number))

        if roll_number == 1: # if point has not been set
            if (val == 4 or val == 5 or val == 6 or val == 8 or val == 9 or val == 10):
                self.console_out("The point is: " + str(val))
            else:
                self.game_over(val)
        
        else:
            if val == self.game.array_rolls[0].get_dice_total():
                self.game_over(val)
            elif val == 7:
                self.game_over(val)
            else:
                pass

    def game_over(self, val):
        roll_number = self.game.get_roll_num()
        #print(str(roll_number))

        if roll_number == 1:
            if val == 7 or val == 11:
                self.console_out("Pass WIN - Dont LOSS")
                self.r1_pass_win += 1
                self.strvar_r1pw.set(str(self.r1_pass_win))
            
            elif val == 2 or val == 3:
                self.console_out("Pass LOSS - Dont WIN")
                self.r1_dont_win += 1
                self.strvar_r1dw.set(str(self.r1_dont_win))
            
            else: # if val is 12
                self.console_out("Pass LOSS - Dont PUSH")

        else:
            if val == 7:
                self.console_out("Pass LOSS - Dont WIN")
                self.after_dont_win += 1
                self.strvar_adw.set(str(self.after_dont_win))
            else:
                self.console_out("Pass WIN - Dont LOSS")
                self.after_pass_win += 1
                self.strvar_apw.set(str(self.after_pass_win))
        
        self.session.add_game(self.game)
        self.game = Game()

    def console_out(self, text_string):
        self.text_console.configure(state="normal")
        self.text_console.insert(tk.END, (text_string + "\n"))
        self.text_console.see(tk.END)
        self.text_console.configure(state="disabled")

if __name__ == "__main__":
    main()