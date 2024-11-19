import turtle as t  # Import the turtle module and alias it as 't' for simplicity
import random  # Import the random module to generate random colors

# Create a turtle object named 'tim'
tim = t.Turtle()

# Set the turtle's color mode to 255 (RGB mode) for a full range of colors
t.colormode(255)

# Function to generate a random RGB color
def random_color():
    r = random.randint(0, 255)  # Generate a random red value
    g = random.randint(0, 255)  # Generate a random green value
    b = random.randint(0, 255)  # Generate a random blue value
    color = (r, g, b)  # Combine the RGB values into a tuple
    return color  # Return the color tuple

# Set the turtle's drawing speed to the fastest for smooth and quick animations
tim.speed("fastest")

# Function to draw a spirograph with a specified gap size between each circle
def draw_spirograph(size_of_gap):
    # Loop to draw circles in a full 360° rotation, with the specified gap
    for i in range(int(360 / size_of_gap)):  
        tim.color(random_color())  # Set a random color for the turtle's pen
        tim.circle(100)  # Draw a circle with a radius of 100 units
        tim.setheading(tim.heading() + size_of_gap)  # Rotate the turtle's heading by the gap size

# Call the function to draw the spirograph with a gap size of 5°
draw_spirograph(5)

# Create a screen object and set it to close when clicked
screen = t.Screen()
screen.exitonclick()
