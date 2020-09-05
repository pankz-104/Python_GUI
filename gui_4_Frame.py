from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)
root.geometry("400x400")
label = Label(root, text = "GUI_Program",fg="red",bg="green")
label.pack()

root.mainloop()
