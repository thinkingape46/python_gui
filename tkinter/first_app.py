from tkinter import *

# This has to happen before anything
root = Tk()

# In tkinter, first we have to define a thing and then display it.

# creating a label
label_one = Label(root, text="Hello World!")

# Then we pack it, it is not something we do later.
label_one.pack()

# Create a loop
root.mainloop()