# grid layout in Tkinter

from tkinter import *

root = Tk()

root.geometry("400x400")

label_1 = Label(root,text="Email")
label_1.grid(row=0,column=0,sticky="e")

label_2 = Label(root,text="Password")
label_2.grid(row=1,column=0,sticky="e")
# sticky options "e","w","n","s" i.e. east, west, north and south

entry_1 = Entry(root)
entry_1.grid(row=0, column=1)

entry_2 = Entry(root)
entry_2.grid(row=1,column=1)

root.mainloop()
