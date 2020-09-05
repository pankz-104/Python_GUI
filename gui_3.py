from tkinter import *
# setting foreground and background colour

root = Tk()
root.geometry("300x400")
label = Label(root, text = "GUI_Program")
label.pack()

label_2 = Label(root,text="setting colors", fg="red",bg="purple")
label_2.pack()

root.mainloop()
