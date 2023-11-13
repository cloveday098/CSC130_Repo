import tkinter as tk
import random

# Constants
WIDTH, HEIGHT = 400, 400
GRAVITY = 1
JUMP_STRENGTH = -10
PIPE_WIDTH = 40
PIPE_SPACING = 100
PIPE_SPEED = 2

# Initialize the main window
root = tk.Tk()
root.title("Flappy Bird")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Create the bird
bird = canvas.create_rectangle(50, HEIGHT//2 - 10, 60, HEIGHT//2 + 10, fill='blue')

# Initialize bird's velocity
bird_velocity = 0

# Create the pipes
pipes = []

# Function to make the bird jump
def jump(event):
    global bird_velocity
    bird_velocity = JUMP_STRENGTH

# Bind the jump function to the spacebar key
root.bind('<space>', jump)

# Function to update the game
def update():
    global bird_velocity, pipes

    # Update bird's position
    canvas.move(bird, 0, bird_velocity)
    bird_velocity += GRAVITY

    # Check if the bird hits the ground
    bird_coords = canvas.coords(bird)
    if bird_coords[3] >= HEIGHT:
        bird_velocity = 0
        canvas.coords(bird, bird_coords[0], HEIGHT - 20, bird_coords[2], HEIGHT)

    # Create and move pipes
    rand = random.randint(1, 100)
    if rand < 5:
        pipe_height = random.randint(50, HEIGHT - PIPE_SPACING - 50)
        top_pipe = canvas.create_rectangle(WIDTH, 0, WIDTH + PIPE_WIDTH, pipe_height, fill='green')
        bottom_pipe = canvas.create_rectangle(WIDTH, pipe_height + PIPE_SPACING, WIDTH + PIPE_WIDTH, HEIGHT, fill='green')
        pipes.append((top_pipe, bottom_pipe))

    new_pipes = []
    for top_pipe, bottom_pipe in pipes:
        canvas.move(top_pipe, -PIPE_SPEED, 0)
        canvas.move(bottom_pipe, -PIPE_SPEED, 0)
        if canvas.coords(top_pipe)[2] > 0:
            new_pipes.append((top_pipe, bottom_pipe))
        else:
            canvas.delete(top_pipe)
            canvas.delete(bottom_pipe)

    pipes = new_pipes

    # Check for collisions
    for top_pipe, bottom_pipe in pipes:
        if canvas.coords(bird)[2] > canvas.coords(top_pipe)[0] and canvas.coords(bird)[0] < canvas.coords(top_pipe)[2]:
            if canvas.coords(bird)[1] < canvas.coords(top_pipe)[3] or canvas.coords(bird)[3] > canvas.coords(bottom_pipe)[1]:
                game_over()

    # Schedule the update function to be called again
    canvas.after(20, update)

# Function to end the game
def game_over():
    canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", fill='red')
    root.unbind('<space>')  # Unbind the jump function

# Start the game loop
update()

root.mainloop()