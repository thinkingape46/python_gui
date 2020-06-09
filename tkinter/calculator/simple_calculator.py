# Import all from tkinter

from tkinter import *

root = Tk()
root.title("Simple Calculator")

temp_string = ""

add_input = []

def enter(x):
    pass

# Create a screen
scr_top = Entry(root, width=32, borderwidth=10, bg="#dedede", fg="#004f3b")
scr_top.grid(row = 0, columnspan = 4)

def btn_rec(num_sym):
    global temp_string
    if num_sym in ["+", "-", "*"]:
        add_input.append(temp_string)
        temp_string = ""
        add_input.append([num_sym])
    else:
        temp_string += str(num_sym)
    scr_top.insert(END, num_sym)

def insert(num):
    scr_top.insert(0, num)

def clear_screen():
    scr_top.delete(0, END)
    global add_input
    add_input = []

def output_screen():
    global temp_string
    global add_input
    add_input.append(temp_string)
    print(add_input)
    result = processing()
    scr_top.delete(0, END)
    scr_top.insert(0, result)
    temp_string = ""
    add_input = []

def processing():
    result = int(add_input[0])
    i = 0
    while i < len(add_input) - 2:
        if add_input[i + 1][0] == "+":        
            result = result + int(add_input[i + 2])
            
        elif add_input[i + 1][0] == "-":
            result = result - int(add_input[i + 2])
            
        elif add_input[i + 1][0] == "*":
            result = result * int(add_input[i + 2])
        i = i + 2
    return result

# create button 7

btn_seven = Button(root, text = "7", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(7))
# add the button_seven to the grid.
btn_seven.grid(row = 1, column = 0)

# Create buttons 6 to 0

btn_eight = Button(root, text = "8", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(8))
btn_eight.grid(row = 1, column = 1)

btn_nine = Button(root, text = "9", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(9))
btn_nine.grid(row = 1, column = 2)

btn_four = Button(root, text = "4", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(4))
btn_four.grid(row = 2, column = 0)

btn_five = Button(root, text = "5", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(5))
btn_five.grid(row = 2, column = 1)

btn_six = Button(root, text = "6", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(6))
btn_six.grid(row = 2, column = 2)

btn_one = Button(root, text = "1", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(1))
btn_one.grid(row = 3, column = 0)

btn_two = Button(root, text = "2", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(2))
btn_two.grid(row = 3, column = 1)

btn_three = Button(root, text = "3", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(3))
btn_three.grid(row = 3, column = 2)

btn_three = Button(root, text = "0", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(0))
btn_three.grid(row = 4, column = 0)

btn_enter = Button(root, text = "Enter", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = output_screen)
btn_enter.grid(row = 4, column = 1)

btn_add = Button(root, text = "+", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec("+"))
btn_add.grid(row = 1, column = 3)

btn_sub = Button(root, text = "-", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec("-"))
btn_sub.grid(row = 2, column = 3)

btn_prod = Button(root, text = "X", state="disabled", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec("*"))
btn_prod.grid(row = 3, column = 3)

btn_prod = Button(root, text = "Clear", bd = 5, width = 5, height = 3, padx = 3, bg = "#b0cfc7", command = clear_screen)
btn_prod.grid(row = 4, column = 2)


root.mainloop()