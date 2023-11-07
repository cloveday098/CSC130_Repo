from tkinter import *
import math

def computeTax():
    gimme = price.get()
    try:
        tax = eval(gimme) * .15
    except:
        if gimme == "e": gimme = math.e
        lbl2.configure(text = "Incorrect input for price")
        lbl2.configure(fg="red")
    print(gimme)

# Create a new window
window = Tk()
window.title("Kill Me But Don't Tax Me!")
window.geometry("600x300")

# Create label, entry box, and button
lbl = Label(window, text = "Enter your restaurant bill")
price = StringVar()
ent = Entry(window, width=80, textvariable=price)
btn = Button(window, cursor = "plus", command=computeTax, text="Compute Tax", fg="red", font=("Arial 18 bold"))
lbl2 = Label(window, text="")

lbl.pack()
ent.pack()
btn.pack()
lbl2.pack()

window.mainloop()