"""
This Ping Pong game is designed as a simple and interactive introduction to game development in Python.
It demonstrates basic concepts such as object creation, event handling, and collision detection.
The game provides a platform for beginners to experiment
 with game development and graphical programming in a fun and engaging way.
"""

import turtle  # Import turtle for creating graphics.
import random  # Import random to generate random numbers.
import keyboard  # Import keyboard to detect keystrokes.
import time  # Import time for delays.

# Function to create a paddle.
def create_paddle(color, x_pos):
    paddle = turtle.Turtle()  # Create a Turtle object for the paddle.
    paddle.shape("square")  # Set the paddle's shape to a square.
    paddle.color(color)  # Set the paddle's color.
    paddle.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle to desired dimensions.
    paddle.penup()  # Lift the pen to avoid drawing lines.
    paddle.goto(x_pos, 0)  # Position the paddle.
    return paddle

# Function to move a paddle up or down.
def move_paddle(paddle, y):
    paddle.sety(y)  # Set the y-coordinate of the paddle.

# Function to create the ball.
def create_ball():
    ball = turtle.Turtle()  # Create a Turtle object for the ball.
    ball.shape("circle")  # Set the ball's shape to a circle.
    ball.color("white")  # Set the ball's color.
    ball.penup()  # Lift the pen to avoid drawing lines.
    ball.goto(0, 0)  # Position the ball at the center.
    ball.dx = random.choice([-0.15, 0.15])  # Set the horizontal speed.
    ball.dy = random.choice([-0.15, 0.15])  # Set the vertical speed.
    ball.stopped = False  # Initialize stopped attribute.
    return ball

# Function to update and display the score.
def update_score():
    score_display.clear()  # Clear the previous score display.
    score_display.write("Blue: {}  Red: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))  # Write the new score.

# Create a turtle for displaying the score.
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

# Set up the screen.
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Ping Pong")
wn.tracer(0)

# Initialize the score for both players.
score_left = 0
score_right = 0

# Set difficulty
difficulty = 10

# Create the left and right paddles and the ball.
left_paddle = create_paddle("blue", -350)
right_paddle = create_paddle("red", 350)
ball = create_ball()

# Main game loop.
while True:
    wn.update()  # Update the screen.

    # Move the ball if it's not stopped.
    if not ball.stopped:
        ball.setx(ball.xcor() + ball.dx)  # Move the ball horizontally.
        ball.sety(ball.ycor() + ball.dy)  # Move the ball vertically.

    # Check if ball is out of bounds
    if ball.xcor() > 390:
        score_left += 1  # Increment the left player's score
        update_score()  # Update the score display
        ball.stopped = True  # Temporarily stop the ball's movement
        ball.goto(0, 0)  # Reset the ball's position to the center
        ball.dx *= -1  # Reverse the ball's horizontal direction
        wn.update()  # Update the window to reflect changes
        time.sleep(2)  # Pause for 2 seconds before resuming play
        ball.stopped = False  # Allow the ball to start moving again

    elif ball.xcor() < -390:
        score_right += 1  # Increment the right player's score
        update_score()  # Update the score display
        ball.stopped = True  # Temporarily stop the ball's movement
        ball.goto(0, 0)  # Reset the ball's position to the center
        ball.dx *= -1  # Reverse the ball's horizontal direction
        wn.update()  # Update the window to reflect changes
        time.sleep(2)  # Pause for 2 seconds before resuming play
        ball.stopped = False  # Allow the ball to start moving again

    # Boundary checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1  # Reverse the ball's vertical direction if it hits top/bottom

    if ball.xcor() > 340 and ball.xcor() < 350 and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)  # Prevent the ball from moving further right
        ball.dx *= -1  # Reverse the ball's horizontal direction
        ball.dx *= (1 + difficulty / 100)  # Increase ball speed when hitting paddle

    if ball.xcor() < -340 and ball.xcor() > -350 and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)  # Prevent the ball from moving further left
        ball.dx *= -1  # Reverse the ball's horizontal direction
        ball.dx *= (1 + difficulty / 100)  # Increase ball speed when hitting paddle

    if ball.xcor() > 390 or ball.xcor() < -390:  # If ball goes out of bounds
        ball.goto(0, 0)  # Reset ball to the center
        ball.dx *= -1  # Reverse the ball's horizontal direction

    # Keyboard controls
    if keyboard.is_pressed('w') and left_paddle.ycor() < 250:
        move_paddle(left_paddle, left_paddle.ycor() + 1)
    if keyboard.is_pressed('s') and left_paddle.ycor() > -240:
        move_paddle(left_paddle, left_paddle.ycor() - 1)
    if keyboard.is_pressed('up') and right_paddle.ycor() < 250:
        move_paddle(right_paddle, right_paddle.ycor() + 1)
    if keyboard.is_pressed('down') and right_paddle.ycor() > -240:
        move_paddle(right_paddle, right_paddle.ycor() - 1)
