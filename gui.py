from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Label(frm,text="new User??").grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)
root.mainloop()