# Dice class module used to draw
class Die():
    def __init__(self, value):
        self.value = value

    def draw(self, canvas):
        canvas.create_rectangle(2, 2, 38, 38, width=1)

        if self.value == 1:
            canvas.create_oval(17, 17, 23, 23, width=1, fill="black")
            
        elif self.value == 2:
            canvas.create_oval(8, 8, 14, 14, width=1, fill="black")
            canvas.create_oval(26, 26, 32, 32, width=1, fill="black")
        
        elif self.value == 3:
            canvas.create_oval(17, 17, 23, 23, width=1, fill="black")
            canvas.create_oval(8, 8, 14, 14, width=1, fill="black")
            canvas.create_oval(26, 26, 32, 32, width=1, fill="black")

        elif self.value == 4:
            canvas.create_oval(8, 8, 14, 14, width=1, fill="black")
            canvas.create_oval(26, 26, 32, 32, width=1, fill="black")

            canvas.create_oval(26, 8, 32, 14, width=1, fill="black")
            canvas.create_oval(8, 26, 14, 32, width=1, fill="black")

        elif self.value == 5:
            canvas.create_oval(17, 17, 23, 23, width=1, fill="black")

            canvas.create_oval(8, 8, 14, 14, width=1, fill="black")
            canvas.create_oval(26, 26, 32, 32, width=1, fill="black")

            canvas.create_oval(26, 8, 32, 14, width=1, fill="black")
            canvas.create_oval(8, 26, 14, 32, width=1, fill="black")

        elif self.value == 6:
            canvas.create_oval(8, 17, 14, 23, width=1, fill="black")
            canvas.create_oval(26, 17, 32, 23, width=1, fill="black")
            
            canvas.create_oval(8, 8, 14, 14, width=1, fill="black")
            canvas.create_oval(26, 26, 32, 32, width=1, fill="black")

            canvas.create_oval(26, 8, 32, 14, width=1, fill="black")
            canvas.create_oval(8, 26, 14, 32, width=1, fill="black")

        canvas.grid(row=0, column=self.value - 1)