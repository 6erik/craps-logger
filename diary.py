import tkinter as tk

HEIGHT = 400
WIDTH = 400

root = tk.Tk()

die1Frame = tk.Frame(root)
die1Num1 = tk.Button(die1Frame, text="1")
die1Num2 = tk.Button(die1Frame, text="2")
die1Num3 = tk.Button(die1Frame, text="3")
die1Num4 = tk.Button(die1Frame, text="4")
die1Num5 = tk.Button(die1Frame, text="5")
die1Num6 = tk.Button(die1Frame, text="6")
die1Num1.pack()
die1Num2.pack()
die1Num3.pack()
die1Num4.pack()
die1Num5.pack()
die1Num6.pack()
die1Frame.pack()

die2Frame = tk.Frame(root)
die2Num1 = tk.Button(die2Frame, text="1")
die2Num2 = tk.Button(die2Frame, text="2")
die2Num3 = tk.Button(die2Frame, text="3")
die2Num4 = tk.Button(die2Frame, text="4")
die2Num5 = tk.Button(die2Frame, text="5")
die2Num6 = tk.Button(die2Frame, text="6")
die2Num1.pack()
die2Num2.pack()
die2Num3.pack()
die2Num4.pack()
die2Num5.pack()
die2Num6.pack()
die2Frame.pack()

root.mainloop()