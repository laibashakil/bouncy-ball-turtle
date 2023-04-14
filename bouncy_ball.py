import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Bouncy Ball")
wn.bgcolor("green")

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.speed(0)
ball.goto(0, 200)

# Set up the ball's initial velocity and gravity
ball.dy = 0
gravity = 0.1

# Define a function to move the ball
def move_ball():
    ball.dy -= gravity  # Apply gravity to the ball's velocity
    ball.sety(ball.ycor() + ball.dy)  # Move the ball based on its velocity

    # Check if the ball has hit the bottom of the screen
    if ball.ycor() < -250:
        ball.dy *= -1  # Reverse the ball's velocity

# Main loop for the game
while True:
    try:
        move_ball()  # Move the ball
    except turtle.Terminator:
        # Catch the "turtle.Terminator" exception that is raised when the user closes the window
        break

# Clean up when the game is over
wn.bye()
