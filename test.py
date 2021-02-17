from tkinter import *

root = Tk()

PlusButton = Button(root, text="+", padx = 15, pady = 15, bg="Light Grey")
MinusButton = Button(root, text="-", padx = 15, pady = 15, bg="Light Grey")
MultiButton = Button(root, text="*", padx = 15, pady = 15, bg="Light Grey")
DivButton = Button(root, text="/", padx = 15, pady = 15, bg="Light Grey")

PlusButton.grid(row = 0, column = 0)
MinusButton.grid(row = 0, column = 1)
MultiButton.grid(row = 1, column = 0)
DivButton.grid(row = 1, column = 1)

root.mainloop()