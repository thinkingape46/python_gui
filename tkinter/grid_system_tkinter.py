from tkinter import *

# grid system is something we will be using all the time.

root = Tk()

# Creating labels

label_zero = Label(root, text="I am Label Zero")
label_one = Label(root, text="I am Label One")

# Instead of packing, we shall using grid system
# We need to specify row and columns.
label_zero.grid(row = 0, column = 0)
label_one.grid(row = 2, column = 1)

# Remember python uses Object oriented program.
# Label is a class with grid as member.
# looks like label_zero is a object.
# grid is a method.


# One thing to remember is, if we change the column to 5,
# it still sits next to column 0, because columns 1,2,3,4 are empty.
root.mainloop()