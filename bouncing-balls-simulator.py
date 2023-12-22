"""
This script creates a "Bouncing Balls Simulation" using Python's turtle module.
It features multiple balls bouncing around the screen with collisions between them and the walls.
The balls change direction and speed upon collisions,
 simulating basic physics principles like gravity and elasticity.
"""

import turtle  # Import the turtle drawing module.
import random  # Import the the random module for math.
import time  # Import the time module.

wn = turtle.Screen()  # Set up the screen.
wn.bgcolor("black")  # Set background color.
wn.title("Bouncing Ball Simulator")  # Set window title.
wn.tracer()  # Turn off automatic updates.

turtle.tracer(0, 0)  # Turn off animation for setup.
balls = []  # List to hold the ball objects.
gravity = 0.1  # Simulate gravity.
elasticity = 0.95  # Simulate elasticity on collision.
multiplier = 1  # Factor for speed change after collision.
speed = 6  # Initial speed range for the balls.

# Create multiple balls.
for _ in range(30):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]  # Possible ball colors.
shapes = ["circle"]  # Possible ball shapes.

# Initialize each ball's properties.
for ball in balls:  # Loops through the number of balls to initialize.
    ball.shape(random.choice(shapes))  # Randomly chooses the balls shape from the shapes list.
    ball.color(random.choice(colors))  # Randomly chooses the balls color from the color list.
    ball.penup()  # Raises pen so not to draw yet.
    ball.speed(0)  # Set turtle drawing to fastest speed.
    x = random.randint(-290, 290)  # Choose random x position within given range.
    y = random.randint(200, 400)  # Choose random y position within given range.
    ball.goto(x, y)  # Moves the raised pen into position.
    ball.dy = 0  # Initialize vertical speed to zero.
    ball.dx = random.randint(-speed, speed)  # Randomly set horizontal speed within the given range.
    ball.da = random.randint(-5,  5)  # Random rotation speed (angular velocity) for the ball.

wn.update()
time.sleep(1)  # Initial pause before starting the simulation.

# Main loop for the animation.
while True:
    time.sleep(0.01)  # Short delay for each iteration of the loop.

    turtle.tracer(0, 0)  # Turn off automatic animation to manually update the screen.
    for ball in balls:
        ball.rt(ball.da)  # Rotate the ball by its angular velocity.
        ball.dy -= gravity  # Apply gravity by decreasing vertical speed.
        ball.sety(ball.ycor() + ball.dy)  # Update the vertical position.
        ball.setx(ball.xcor() + ball.dx)  # Update the horizontal position.

        # Wall collision checks.
        if ball.xcor() > 300 or ball.xcor() < -300:
            ball.dx *= -1 * elasticity  # Reverse and reduce horizontal speed upon collision.
            ball.da *= -1 * elasticity  # Reverse and reduce angular velocity upon collision.

        # Ceiling and floor collision checks.
        if ball.ycor() > 300 or ball.ycor() < -300:
            ball.sety(300 if ball.ycor() > 0 else -300)  # Reset the ball position to within bounds.
            ball.dy *= -1 * elasticity  # Reverse and reduce vertical speed upon collision.
            ball.da *= -1 * elasticity  # Reverse and reduce angular velocity upon collision.

    # Check collisions between balls.
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if balls[i].distance(balls[j]) < 20:  # Check if two balls are close enough to collide.
                # Swap the velocities of the colliding balls.
                balls[i].dx, balls[j].dx = balls[j].dx * multiplier, balls[i].dx * multiplier
                balls[i].dy, balls[j].dy = balls[j].dy * multiplier, balls[i].dy * multiplier

    wn.update()  # Manually update the screen with the new positions.
