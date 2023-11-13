import tkinter as tk
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
SHIP_SIZE = 20
BULLET_SPEED = 5
ASTEROID_SPEED = 1
ASTEROID_RADIUS = 30

# Initialize the main window
root = tk.Tk()
root.title("Asteroids")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Create the spaceship
ship = canvas.create_polygon(
    10, 0,
    -10, 10,
    -5, 0,
    -10, -10,
    10, 0,
    fill='blue'
)
canvas.move(ship, WIDTH/2, HEIGHT/2)

# Initialize ship's angle and velocity
ship_angle = 0
ship_velocity_x = 0
ship_velocity_y = 0

# Create a list to store the bullets
bullets = []

# Function to move the ship
def move_ship(event):
    global ship_angle, ship_velocity_x, ship_velocity_y
    if event.keysym == 'Up':
        ship_angle = math.radians(-canvas.coords(ship)[2])
        ship_velocity_x += math.cos(ship_angle) * 2
        ship_velocity_y += math.sin(ship_angle) * 2
    elif event.keysym == 'Left':
        ship_angle += math.radians(20)
    elif event.keysym == 'Right':
        ship_angle -= math.radians(20)
    else:
        ship_velocity_x -= math.cos(ship_angle) * 2
        ship_velocity_y -= math.sin(ship_angle) * 2

# Function to fire a bullet
def fire(event):
    global bullets
    x, y = canvas.coords(ship)[0], canvas.coords(ship)[1]
    angle = math.degrees(ship_angle)
    bullet = canvas.create_oval(x, y, x + 5, y + 5, fill='red')
    bullets.append((bullet, angle))

# Function to update the game
def update():
    global ship_velocity_x, ship_velocity_y, bullets

    # Move the ship
    canvas.move(ship, ship_velocity_x, ship_velocity_y)

    # Move the bullets
    new_bullets = []
    for bullet, angle in bullets:
        x_speed = BULLET_SPEED * math.cos(math.radians(angle))
        y_speed = BULLET_SPEED * math.sin(math.radians(angle))
        canvas.move(bullet, x_speed, y_speed)

        # Check if the bullet is out of bounds
        x, y = canvas.coords(bullet)[0], canvas.coords(bullet)[1]
        if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
            canvas.delete(bullet)
        else:
            new_bullets.append((bullet, angle))
    bullets = new_bullets

    # Schedule the update function to be called again
    canvas.after(20, update)

# Bind keys to functions
root.bind('<Up>', move_ship)
root.bind('<Left>', move_ship)
root.bind('<Right>', move_ship)
root.bind('<Down>', move_ship)
root.bind('<space>', fire)

# Start the game loop
update()

root.mainloop()