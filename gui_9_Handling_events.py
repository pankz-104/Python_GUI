# Handling Events

from tkinter import *

def left(event):
    print("You jave clicked left button !!")

def middle(event):
    print("You have clicked middle mouse button !!")
          
def right(event):
    print("You have clicked right button !!")


root = Tk()
root.geometry("500x500")
frame = Frame(root,width=400, height=400)
frame.bind("<Button-1>",left)
frame.bind("<Button-3>",right)
frame.bind("<Button-2>",middle)
frame.pack()


root.mainloop()
