import tkinter as tk

HEIGHT = 400
WIDTH = 400

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

button = tk.Button(root, text="Test button")
button.pack()

root.mainloop()