# Import all from tkinter

from tkinter import *

root = Tk()
root.title("Simple Calculator")

# adding an icon
root.iconbitmap("D:/Learning/GitHub/python_gui/tkinter/calculator/calculator.ico")

# This is a string that stores all the keys strokes "0 to 9,+,-,*".
# The reason this temp_string utilized is, to accept multiple digit numbers.
# The temp_string concatenate the number entered by user.
# When an arithmetic operator is enter by the user, this chain breaks and the string is added to "add_input"
temp_string = ""

# Below list stores all the numbers and arithmetic operators as item, the items are in order as entered by the user.
add_input = []

def enter(x):
    pass

# Create a screen that displays input and output.
scr_top = Entry(root, width=40, borderwidth=10, bg="#dedede", fg="#004f3b")
scr_top.grid(row = 0, columnspan = 4)

def btn_rec(num_sym):

    # import global temp_string
    global temp_string

    # below 'if' statement runs whenver arithmetic is entered.
    if num_sym in ["+", "-", "*"]:

        # Below line appends the previously enter number or operator to the "add_input" list and empties the string.
        # This is done so that the opertor doesn't sit next to another operator.
        add_input.append(temp_string)
        temp_string = ""

        # The operator is now add to the list "add_input"
        add_input.append([num_sym])

    # below else statement runs when a number is entered by the user and not an arithmetic operator.
    else:
        # The number entered by the user is concatenated to "temp_string".
        temp_string += str(num_sym)
    scr_top.insert(END, num_sym)

def insert(num):
    scr_top.insert(0, num)

# This function runs when clear button is entered by the user.
# It clear the scr_top entry and add_input list.
def clear_screen():
    scr_top.delete(0, END)
    global add_input
    add_input = []

# This function runs when the button "enter" is clicked.
def output_screen():
    global temp_string
    global add_input

    # Add the last entered number to add_input.
    add_input.append(temp_string)
    print(add_input)

    # Now the add_input list is ready for processing()
    result = processing()

    # scr_top entry is deleted.
    scr_top.delete(0, END)

    # scr_top entry is updated with results.
    scr_top.insert(0, result)
    temp_string = ""
    add_input = []

def processing():
    multiply(add_input)
    result = int(add_input[0])
    i = 0
    while i < len(add_input) - 2:
        if add_input[i + 1][0] == "+":        
            result = result + int(add_input[i + 2])
            
        elif add_input[i + 1][0] == "-":
            result = result - int(add_input[i + 2])
            
        else:
            break
        i = i + 2
    return result

def multiply(add_input):
    while ["*"] in add_input:
        i = add_input
        index = i.index(["*"])
        y = int(i[index - 1])*int(i[index + 1])
        for j in range(0, 3):
            i.pop(index - 1)
        i.insert(index - 1, y)
    add_input = i
    return add_input

# Creation of all the buttons on the screen.,

btn_seven = Button(root, text = "7", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(7))
# add the button_seven to the grid.
btn_seven.grid(row = 1, column = 0)

btn_eight = Button(root, text = "8", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(8))
btn_eight.grid(row = 1, column = 1)

btn_nine = Button(root, text = "9", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(9))
btn_nine.grid(row = 1, column = 2)

btn_four = Button(root, text = "4", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(4))
btn_four.grid(row = 2, column = 0)

btn_five = Button(root, text = "5", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(5))
btn_five.grid(row = 2, column = 1)

btn_six = Button(root, text = "6", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(6))
btn_six.grid(row = 2, column = 2)

btn_one = Button(root, text = "1", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(1))
btn_one.grid(row = 3, column = 0)

btn_two = Button(root, text = "2", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(2))
btn_two.grid(row = 3, column = 1)

btn_three = Button(root, text = "3", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(3))
btn_three.grid(row = 3, column = 2)

btn_three = Button(root, text = "0", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec(0))
btn_three.grid(row = 4, column = 0)

btn_enter = Button(root, text = "Enter", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = output_screen)
btn_enter.grid(row = 4, column = 1)

btn_add = Button(root, text = "+", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec("+"))
btn_add.grid(row = 1, column = 3)

btn_sub = Button(root, text = "-", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec("-"))
btn_sub.grid(row = 2, column = 3)

btn_prod = Button(root, text = "X", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = lambda: btn_rec("*"))
btn_prod.grid(row = 3, column = 3)

btn_prod = Button(root, text = "Clear", bd = 6, width = 6, height = 3, padx = 3, bg = "#b0cfc7", command = clear_screen)
btn_prod.grid(row = 4, column = 2)

root.mainloop()
