"""
This script creates a window with a grid of animated turtles.
Each turtle, an instance of the Player class, cycles through different shapes at set intervals.
The script demonstrates basic object-oriented programming, animation with turtle,
and window management in Python.
"""

import turtle  # Import the turtle module for creating graphics.
import time    # Import the time module for controlling animation timing.

# Set up the window
wn = turtle.Screen()  # Create a screen object for the window.
wn.title("Animation Demo")  # Set the title of the window.
wn.bgcolor("black")  # Set the background color of the window.

# Define the Player class
class Player(turtle.Turtle):  # Player class inherits from turtle.Turtle.
    def __init__(self):
        super().__init__()  # Initialize the superclass (turtle.Turtle).
        self.penup()  # Lift the pen up to prevent drawing lines.
        self.shape("circle")  # Set the initial shape of the turtle.
        self.color("green")  # Set the color of the turtle.
        self.frame = 0  # Initialize a frame counter.
        self.frames = ["circle", "triangle", "square"]  # Define a list of shapes to cycle through.

    def animate(self):
        self.frame = (self.frame + 1) % len(self.frames)  # Increment the frame and loop back to 0 if it exceeds the number of shapes.
        self.shape(self.frames[self.frame])  # Update the turtle's shape based on the current frame.
        wn.ontimer(self.animate, 500)  # Schedule the next call to animate after 500 milliseconds.

# Create a single player instance and animate
player = Player()  # Create an instance of Player.
player.animate()   # Start the animation process.

# Main loop to keep the window open
while True:
    wn.update()  # Continuously update the window to reflect changes.
    time.sleep(0.1)  # Short sleep to prevent the program from using too many resources.
