# Import everything from tkiner.



from tkinter import *

root = Tk()

def clik_zero():
    greeting = "Hello "+ entry_zero.get() + "!"  
    label_zero = Label(root, text=greeting)
    label_zero.pack()  

# Creating of an entery.
entry_zero = Entry(root, width=50, borderwidth=10, bg="#dedede", fg="#004f3b")

# Pack the entry box.
entry_zero.pack()
# Placeholder text
entry_zero.insert(0, "Enter your name here:")

button_zero = Button(root, text="Enter Your Name", padx = 20, pady = 10, fg = "#ffffff", bg="#858585", command=clik_zero)
button_zero.pack()

root.mainloop()
