from tkinter import *
from PIL import Image, ImageTk
import random

# Init
w, h = 400, 400
cell_size = 20
pacSize = 20
ghostSize = 20

root = Tk()
root.title("Pac-Man")
canvas = Canvas(root, width=w, height=h)
canvas.pack()

# Background
bgImg = Image.open("pacManbg.png")
resize_bg = bgImg.resize((1400, 800))
bgImg = ImageTk.PhotoImage(resize_bg)
bgImglbl = Label(root, image=bgImg)
bgImglbl.place(x=20, y=0)

# Pacman
pacman = canvas.create_oval(0, 0, pacSize, pacSize, fill='yellow')
canvas.move(pacman, w/2 - pacSize/2, h/2 - pacSize/2)


root.mainloop()