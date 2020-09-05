# Creating menus and sub menus in Tkinter



from tkinter import *

def work():
    print("Funciton is working")

def Edit():
    print("This is under edit_menu")

def res():
    print("GUI Window Resized")
    root.geometry("200x100")

def norm():
    print("GUI Window back to normal")
    root.geometry("400x400")
    
root = Tk()
root.geometry("400x400")
menu_1 = Menu(root)
root.config(menu=menu_1)

# First menu
file_menu = Menu(menu_1)
menu_1.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New File",command=work)
file_menu.add_cascade(label="Open")
file_menu.add_cascade(label="Save")
file_menu.add_cascade(label="Save as")
file_menu.add_cascade(label="Exit")


# Second menu
edit_menu = Menu(menu_1)
menu_1.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="Cut",command=Edit)
edit_menu.add_cascade(label="Copy")
edit_menu.add_cascade(label="Paste")
edit_menu.add_cascade(label="Rename")
edit_menu.add_command(label="Resize",command=res)
edit_menu.add_command(label="Normal",command=norm)

#Third menu
view = Menu(menu_1)
menu_1.add_cascade(label="View", menu=view)

#Fourth menu
Code_menu = Menu(menu_1)
menu_1.add_cascade(label="Code", menu=Code_menu)

#Fifth menu
Run_menu = Menu(menu_1)
menu_1.add_cascade(label="Run", menu=Run_menu)

#Sixth menu
Help_menu = Menu(menu_1)
menu_1.add_cascade(label="Help",menu=Help_menu)

# Add status bar
status = Label(root, text="Run", bg="yellow",
               anchor="w",relief=SUNKEN,bd=1)
status.pack(side=BOTTOM,fill=X)


root.mainloop()
