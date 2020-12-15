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
        
        # TK Variables to update labels
        self.die1value = 0
        self.die2value = 0
        self.strvar_r1pw = tk.StringVar()
        self.strvar_r1dw = tk.StringVar()
        self.strvar_apw = tk.StringVar()
        self.strvar_adw = tk.StringVar()

        # Statistics Variables
        self.r1_pass_win = 0
        self.r1_dont_win = 0
        self.after_pass_win = 0
        self.after_dont_win = 0

        # Call method to create all GUI widgets
        self.create_widgets()

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

        canvas_die1 = tk.Canvas(frame_die1, width=40, height=40)
        canvas_die2 = tk.Canvas(frame_die1, width=40, height=40)
        canvas_die3 = tk.Canvas(frame_die1, width=40, height=40)
        canvas_die4 = tk.Canvas(frame_die1, width=40, height=40)
        canvas_die5 = tk.Canvas(frame_die1, width=40, height=40)
        canvas_die6 = tk.Canvas(frame_die1, width=40, height=40)

        canvas_die1.bind('<Button-1>', lambda  v: self.select_die_1(1))
        canvas_die2.bind('<Button-1>', lambda  v: self.select_die_1(2))
        canvas_die3.bind('<Button-1>', lambda  v: self.select_die_1(3))
        canvas_die4.bind('<Button-1>', lambda  v: self.select_die_1(4))
        canvas_die5.bind('<Button-1>', lambda  v: self.select_die_1(5))
        canvas_die6.bind('<Button-1>', lambda  v: self.select_die_1(6))

        img_die1 = Die(1)
        img_die2 = Die(2)
        img_die3 = Die(3)
        img_die4 = Die(4)
        img_die5 = Die(5)
        img_die6 = Die(6)

        img_die1.draw(canvas_die1)
        img_die2.draw(canvas_die2)
        img_die3.draw(canvas_die3)
        img_die4.draw(canvas_die4)
        img_die5.draw(canvas_die5)
        img_die6.draw(canvas_die6)

        label_die2 = tk.Label(frame_dice_select, text="Die 2: ")
        label_die2.grid(row=1, column=0)

        canvas2_die1 = tk.Canvas(frame_die2, width=40, height=40)
        canvas2_die2 = tk.Canvas(frame_die2, width=40, height=40)
        canvas2_die3 = tk.Canvas(frame_die2, width=40, height=40)
        canvas2_die4 = tk.Canvas(frame_die2, width=40, height=40)
        canvas2_die5 = tk.Canvas(frame_die2, width=40, height=40)
        canvas2_die6 = tk.Canvas(frame_die2, width=40, height=40)

        canvas2_die1.bind('<Button-1>', lambda  v: self.select_die_2(1))
        canvas2_die2.bind('<Button-1>', lambda  v: self.select_die_2(2))
        canvas2_die3.bind('<Button-1>', lambda  v: self.select_die_2(3))
        canvas2_die4.bind('<Button-1>', lambda  v: self.select_die_2(4))
        canvas2_die5.bind('<Button-1>', lambda  v: self.select_die_2(5))
        canvas2_die6.bind('<Button-1>', lambda  v: self.select_die_2(6))

        img_die1.draw(canvas2_die1)
        img_die2.draw(canvas2_die2)
        img_die3.draw(canvas2_die3)
        img_die4.draw(canvas2_die4)
        img_die5.draw(canvas2_die5)
        img_die6.draw(canvas2_die6)

        button_submit = tk.Button(frame_submit, text="Submit", command=lambda : self.submit_dice(self.die1value, self.die2value), height=5, width=6)
        button_submit.pack()

        ### Frame - Statistics
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

        ### Frame - Text console
        self.frame_console = tk.Frame(frame_main)
        self.frame_console.grid(row=1)

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
            self.game.add_roll(roll)

            self.console_out("Gm "+ str(game_number + 1) + "- Rd " + str(roll_number + 1) + ": " + str(d1) + " " + str(d2))
            self.make_game_decision(roll)

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
        
        # Add completed game to session, create new Game instance
        self.session.add_game(self.game)
        self.game = Game()

    def console_out(self, text_string):
        self.text_console.configure(state="normal")
        self.text_console.insert(tk.END, (text_string + "\n"))
        self.text_console.see(tk.END)
        self.text_console.configure(state="disabled")

    def select_die_1(self, value):
        self.die1value = value
        self.console_out("selected die 1:  " + str(value))

    def select_die_2(self, value):
        self.die2value = value
        self.console_out("selected die 2:  " + str(self.die2value))

if __name__ == "__main__":
    main()