import tkinter as tk
import tkinter.scrolledtext as st
from die import Die
from roll import Roll
from game import Game
from session import Session

def main():
    # Create App instance, craps_logger
    craps_logger = App()

    # Start GUI event loop
    craps_logger.root.mainloop()

class App:
    def __init__(self):
        self.session = Session()
        self.game = Game()

        self.root = tk.Tk()
        self.root.title("Craps Logger")

        self.orig_color = self.root.cget("background")
        
        # Variables to track dice
        self.die1value = 0
        self.die2value = 0

        # TK Variables to update labels
        self.strvar_r1pw = tk.StringVar()
        self.strvar_r1dw = tk.StringVar()
        self.strvar_apw = tk.StringVar()
        self.strvar_adw = tk.StringVar()
        self.strvar_c1 = tk.StringVar()
        self.strvar_c2 = tk.StringVar()
        self.strvar_c3 = tk.StringVar()
        self.strvar_c4 = tk.StringVar()
        self.strvar_c5 = tk.StringVar()
        self.strvar_c6 = tk.StringVar()

        # Widget Arrays
        self.canvas1_dice = []
        self.canvas2_dice = []

        # Call method to create all GUI widgets
        self.create_widgets()
        self.update_statistics()

    def create_widgets(self):
        # Using 'frame_main' to pack all subframes
        frame_main = tk.Frame(self.root)
        frame_main.pack()

        ### Frame - Dice select
        frame_dice_select = tk.Frame(frame_main)
        frame_dice_select.grid(row=0, column=0)

        ## Subframe - Die1 & Die2
        frame_die1 = tk.Frame(frame_dice_select)
        frame_die1.grid(row=0, column=1)
        frame_die2 = tk.Frame(frame_dice_select)
        frame_die2.grid(row=1, column=1)
        frame_submit = tk.Frame(frame_dice_select)
        frame_submit.grid(row=0, column=2)

        label_die1 = tk.Label(frame_dice_select, text="Die 1: ")
        label_die1.grid(row=0, column=0)

        label_die2 = tk.Label(frame_dice_select, text="Die 2: ")
        label_die2.grid(row=1, column=0)

        for i in range(6):
            def make_lambda(die, index):
                return lambda v: self.select_die(die, index+1)

            frame_die_x = tk.Canvas(frame_die1, width=40, height=40)
            self.canvas1_dice.append(frame_die_x)
            self.canvas1_dice[i].bind('<Button-1>', make_lambda(1, i))

            frame_die_y = tk.Canvas(frame_die2, width=40, height=40)
            self.canvas2_dice.append(frame_die_y)
            self.canvas2_dice[i].bind('<Button-1>', make_lambda(2, i))

            die = Die(i+1)
            die.draw(self.canvas1_dice[i])
            die.draw(self.canvas2_dice[i])
            
        button_submit = tk.Button(frame_submit, text="Submit", command=lambda : self.submit_dice(self.die1value, self.die2value), height=5, width=6)
        button_submit.pack()

        ### Frame - Statistics
        frame_statistics = tk.Frame(frame_main)
        frame_statistics.grid(row=1, column=1, padx=(0, 15), pady=(5, 5))

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

        label_frequencies = tk.Label(frame_statistics, text="Frequencies")
        label_frequencies.grid(row=5, column=1)

        self.label_count_1 = tk.Label(frame_statistics, text="1")
        self.label_count_1.grid(row=6, column=0)

        self.label_count_2 = tk.Label(frame_statistics, text="2")
        self.label_count_2.grid(row=7, column=0)

        self.label_count_3 = tk.Label(frame_statistics, text="3")
        self.label_count_3.grid(row=8, column=0)

        self.label_count_4 = tk.Label(frame_statistics, text="4")
        self.label_count_4.grid(row=9, column=0)

        self.label_count_5 = tk.Label(frame_statistics, text="5")
        self.label_count_5.grid(row=10, column=0)

        self.label_count_6 = tk.Label(frame_statistics, text="6")
        self.label_count_6.grid(row=11, column=0)

        self.label_c1 = tk.Label(frame_statistics, textvariable=self.strvar_c1)
        self.label_c1.grid(row=6, column=2)

        self.label_c2 = tk.Label(frame_statistics, textvariable=self.strvar_c2)
        self.label_c2.grid(row=7, column=2)

        self.label_c3 = tk.Label(frame_statistics, textvariable=self.strvar_c3)
        self.label_c3.grid(row=8, column=2)

        self.label_c4 = tk.Label(frame_statistics, textvariable=self.strvar_c4)
        self.label_c4.grid(row=9, column=2)

        self.label_c5 = tk.Label(frame_statistics, textvariable=self.strvar_c5)
        self.label_c5.grid(row=10, column=2)

        self.label_c6 = tk.Label(frame_statistics, textvariable=self.strvar_c6)
        self.label_c6.grid(row=11, column=2)

        ### Frame - Text console
        self.frame_console = tk.Frame(frame_main)
        self.frame_console.grid(row=1, padx=(10, 10), pady=(10, 10))

        self.text_console = st.ScrolledText(self.frame_console)
        self.text_console.configure(state="disabled", font=("Arial", 9))
        self.text_console.pack()

    ### Method definitions
    def submit_dice(self, d1, d2):
        roll_number = self.game.get_roll_num()
        game_number = self.session.get_game_num()

        # Check if radio buttons were selected (0 if unselected)
        if (d1 > 0 and d2 > 0):
            roll = Roll(d1, d2)
            self.session.process_roll(roll)
            self.game.add_roll(roll)

            self.console_out("Gm "+ str(game_number + 1) + "- Rd " + str(roll_number + 1) + ": " + str(d1) + " " + str(d2))
            self.make_game_decision(roll)
            self.update_statistics()

        else:
            self.console_out("Select dice values before submitting")


    def make_game_decision(self, roll):
        val = roll.get_dice_total()
        roll_number = self.game.get_roll_num()

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
        winner = ""

        if roll_number == 1:
            if val == 7 or val == 11:
                self.console_out("Pass WIN - Dont LOSS")
                winner = "pass"
            
            elif val == 2 or val == 3:
                self.console_out("Pass LOSS - Dont WIN")
                winner = "dont"
            
            else: # if val is 12
                self.console_out("Pass LOSS - Dont PUSH")
                winner = "push"

        else:
            if val == 7:
                self.console_out("Pass LOSS - Dont WIN")
                winner = "dont"

            else:
                self.console_out("Pass WIN - Dont LOSS")
                winner = "pass"

        self.session.set_winner(winner, roll_number)
        
        # Add completed game to session, create new Game instance
        self.session.add_game(self.game)
        self.game = Game()

    def console_out(self, text_string):
        self.text_console.configure(state="normal")
        self.text_console.insert(tk.END, (text_string + "\n"))
        self.text_console.see(tk.END)
        self.text_console.configure(state="disabled")

    def select_die(self, die, value):
        if die == 1:
            self.die1value = value

            for i in range(6):
                if i == value - 1:
                    self.canvas1_dice[i].configure(bg="white")
                else:
                    self.canvas1_dice[i].configure(bg=self.orig_color)

        elif die == 2:
            self.die2value = value

            for i in range(6):
                if i == value - 1:
                    self.canvas2_dice[i].configure(bg="white")
                else:
                    self.canvas2_dice[i].configure(bg=self.orig_color)
            
        #self.console_out("selected die " + str(die) + ": " + str(value))

    def update_statistics(self):
        self.strvar_r1pw.set(self.session.get_round1_pass_wins())
        self.strvar_r1dw.set(self.session.get_round1_dont_wins())
        self.strvar_apw.set(self.session.get_after_pass_wins())
        self.strvar_adw.set(self.session.get_after_dont_wins())
        self.strvar_c1.set(self.session.get_count_val(1))
        self.strvar_c2.set(self.session.get_count_val(2))
        self.strvar_c3.set(self.session.get_count_val(3))
        self.strvar_c4.set(self.session.get_count_val(4))
        self.strvar_c5.set(self.session.get_count_val(5))
        self.strvar_c6.set(self.session.get_count_val(6))

if __name__ == "__main__":
    main()
