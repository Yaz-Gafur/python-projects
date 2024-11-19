import turtle as t  # Import the turtle module and alias it as 't' for simplicity
import random  # Import the random module to generate random numbers

# Create a turtle object named 'tim'
tim = t.Turtle()

# Set the turtle's color mode to 255 (RGB) to use full range of colors
t.colormode(255)

# Function to generate a random RGB color
def random_color():
    r = random.randint(0, 255)  # Generate a random red value
    g = random.randint(0, 255)  # Generate a random green value
    b = random.randint(0, 255)  # Generate a random blue value
    return (r, g, b)  # Return the color as an (r, g, b) tuple

# List of possible directions for the turtle to face (in degrees)
directions = [0, 90, 180, 270]

# Set the pen size to 10 for thicker lines
tim.pensize(10)

# Set the turtle's speed to the fastest setting
tim.speed("fastest")

# Loop 200 times to create the random walk
for i in range(200):
    tim.color(random_color())  # Set the turtle's pen color to a random color
    tim.forward(30)  # Move the turtle forward by 30 units
    tim.setheading(random.choice(directions))  # Change the turtle's direction randomly
