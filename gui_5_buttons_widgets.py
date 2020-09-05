# buttons and widgets in gui

from tkinter import *

root = Tk()

root.geometry("400x300")
top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

button_1 = Button(top_frame, text="File",fg="blue")
button_1.pack(side=LEFT)
button_2 = Button(top_frame, text="Edit",fg="red")
button_2.pack(side=LEFT)
button_3 = Button(top_frame, text="View",fg="green")
button_3.pack(side=LEFT)
button_4 = Button(top_frame, text="Help",fg="black")
button_4.pack(side=LEFT)

label_1 = Label(root,text="Welcome to gui",bg="blue")
label_1.pack(side=LEFT,fill=Y)

label_2 = Label(root,text="Thnaks!!",bg="red")
label_2.pack(side=BOTTOM,fill=X,padx=45,pady=45)
root.mainloop()
