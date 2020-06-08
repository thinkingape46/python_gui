# import everything from tkinter

from tkinter import *

# root
root = Tk()

# Make a button to do something.
def my_click():
    my_label = Label(root, text="I am a label")
    my_label.pack()

# We wanted in the root.
# We don't use paranthesis for calling a function with command.
button_zero = Button(root, text="ButtonZero", padx = 30, pady = 20, command=my_click, fg="#ffffff", bg="grey")
# We can add a state to the button, such as "disabled"
# Adding padding
button_one = Button(root, text="ButtonOne", state="disabled", padx = 50, pady = 20)

button_zero.pack()
button_one.pack()

root.mainloop()