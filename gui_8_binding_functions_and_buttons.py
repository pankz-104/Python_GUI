# binding funcitons to buttons

from tkinter import *

def subscribe():
    print("Joining function in python !!")
    


root = Tk()
root.geometry("400x400")
button_1 = Button(root,text="Join now", command=subscribe)
button_1.pack()

button_2 = Button(root, text="Exit",command=root.quit)
button_2.pack()

root.mainloop()
