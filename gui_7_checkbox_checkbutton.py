# checkbox and checkbuttn in Tkinter

from tkinter import *

root = Tk()

root.geometry("400x400")

label_1 = Label(root, text="Email")
label_1.grid(row=0,column=0,sticky="e")

label_2 = Label(root, text="Password")
label_2.grid(row=1,column=0, sticky="e")

entry_1 = Entry(root)
entry_1.grid(row=0,column=1)

entry_2 = Entry(root)
entry_2.grid(row=1, column=1)

check=Checkbutton(root,text="Remind me!")
check.grid(row=3,column=1)
button = Button(root,text="Submit!")
button.grid(row=4,column=0)

root.mainloop()
