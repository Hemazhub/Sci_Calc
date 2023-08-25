import tkinter as tk

#math module is imported to perform all the mathematical operations
from math import *

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))     #eval() function is used to evaluate the mathematical expression obtained from the screen variable
            screen.set(result)                   #If the evaluation is successful, the result is converted to a string and displayed
        except Exception as e:
            screen.set("Error")                  # Else displays error

    elif text == "C":
        screen.set("")                           #if "c" text then screen is cleared

    else:
        screen.set(screen.get() + text)

window = tk.Tk()
window.title("Scientific Calculator")
window.configure(background="thistle")

#Entry display tab
screen = tk.StringVar()
entry = tk.Entry(master = window, textvar=screen, font=("DM Sans", 20), justify="right", width = 20)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# To create the buttons in the calculator
buttons = [
    ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("sqrt", 1, 3),
    ("^2", 2, 0), ("pi", 2, 1), ("e", 2, 2), ("log", 2, 3),
    ("^", 3, 0), ("(", 3, 1), (")", 3, 2), ("/", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("*", 4, 3),
    ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("-", 5, 3),
    ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("+", 6, 3),
    ("C", 7, 0), ("0", 7, 1), (".", 7, 2), ("=", 7, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(master=window, text=text, font=("DM Sans", 15), relief="raised", width =7,height = 1)
    button.grid(row=row, column=col, padx=0, pady=0)        #padx, pady = horizontal & vertical padding
    button.bind("<Button>", click)     #The click function handles button clicks and performs mathematical calculations.

window.mainloop()

