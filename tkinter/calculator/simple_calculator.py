# Import all from tkinter

from tkinter import *

root = Tk()
root.title("Simple Calculator") 

opp_input = []

def enter(x):
    pass

# Create a screen
scr_top = Entry(root, width=50, borderwidth=10, bg="#dedede", fg="#004f3b")
scr_top.grid(row = 0, columnspan = 4)

def insert(num):
    scr_top.insert(0, num)

def clear_screen():
    scr_top.delete(0, END)

def output_screen():
    x = scr_top.get()
    scr_top.insert(0, x)

# create button 7

btn_seven = Button(root, text = "7", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 7))
# add the button_seven to the grid.
btn_seven.grid(row = 1, column = 0)

# Create buttons 6 to 0

btn_eight = Button(root, text = "8", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 8))
btn_eight.grid(row = 1, column = 1)

btn_nine = Button(root, text = "9", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 9))
btn_nine.grid(row = 1, column = 2)

btn_four = Button(root, text = "4", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 4))
btn_four.grid(row = 2, column = 0)

btn_five = Button(root, text = "5", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 5))
btn_five.grid(row = 2, column = 1)

btn_six = Button(root, text = "6", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 6))
btn_six.grid(row = 2, column = 2)

btn_one = Button(root, text = "1", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 1))
btn_one.grid(row = 3, column = 0)

btn_two = Button(root, text = "2", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 2))
btn_two.grid(row = 3, column = 1)

btn_three = Button(root, text = "3", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 3))
btn_three.grid(row = 3, column = 2)

btn_three = Button(root, text = "0", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, 0))
btn_three.grid(row = 4, column = 0)

btn_enter = Button(root, text = "Enter", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = output_screen)
btn_enter.grid(row = 4, column = 1)

btn_add = Button(root, text = "+", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, "+"))
btn_add.grid(row = 1, column = 3)

btn_sub = Button(root, text = "-", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, "-"))
btn_sub.grid(row = 2, column = 3)

btn_prod = Button(root, text = "X", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = lambda: scr_top.insert(END, "*"))
btn_prod.grid(row = 3, column = 3)

btn_prod = Button(root, text = "Clear", bd = 5, width = 10, height = 5, padx = 3, bg = "#b0cfc7", command = clear_screen)
btn_prod.grid(row = 4, column = 2)


root.mainloop()