# Better in Pink
from tkinter import *
result = ""
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end="\t")
        result += str(i*j) + "\t"
    print()
    result += "\n"

window = Tk() # Starts a new window
window.configure(background="Black")

# Header for the top
txt = Label(window, text="Ellie's Table", fg="Pink", bg = "Black", font="Calibri 32 bold")
txt.grid(row=0, column=0)

# Prints out the reulting table to the window
box = Label(window, text=result, fg="Pink", bg = "Black", font="Calibri 18")
box.grid(row=1, column=0)

window.mainloop() # Calls the window