from tkinter import *
from tkinter import ttk

#Creates Window
root = Tk()
root.title("Personal Finance")

frm = ttk.Frame(root, padding=100)
frm.grid()

#Adds text to window
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Label(frm,text="new User??").grid(column=1, row=1)

#Creates a button to exit application
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)

#Starts the gui
root.mainloop()