"""     The Hirst Painting Program using Turtle GUI ------

        This program makes a painting which looks exactly like Damien Hirst's 'Lactulose'
        using Turtle method's GUI.
        The painting is 10x10 dots of random colours from Hirst's original painting,'Lactulose'.
        Each dot has a radius of 20 units and gap between 2 consecutive dots is 50 spaces.
"""

import random
import turtle as t

# List of tuples containing RGB values of colours used in Hirst's painting.
color_list = [(26, 109, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (222, 137, 176), (143, 109, 57), (101, 197, 219), (206, 166, 29), (21, 58, 132), (212, 75, 91), (238, 89, 49), (141, 208, 227), (119, 192, 141), (6, 160, 87), (4, 186, 179), (106, 108, 198), (136, 29, 72), (98, 51, 37), (25, 153, 211), (228, 168, 188), (153, 213, 195), (173, 186, 221), (234, 174, 162), (30, 91, 95), (87, 47, 34), (34, 46, 84)]
t.colormode(255)

timmy = t.Turtle()
timmy.speed("fastest")

# Since the turtle starts at mid of the canvas, we change its position
# to fit our 10x10 grid withing the canvas without expanding its size.
timmy.setheading(225)   # Sets heading to an angle of 255.
timmy.penup()           # Don't draw while moving forward.
timmy.forward(300)      # Move forward by 300 spaces and reach the bottom left corner of canvas.
timmy.setheading(0)     # Make the turtle face north once again (set the heading to default).

# Setting the position for 10 rows.
for _ in range(10):
    # Printing 10 rows.
    for _ in range(10):
        timmy.pendown()   # Start drawing on canvas.
        timmy.dot(20, random.choice(color_list))   # Draw a dot of radius 20 having a random color.
        timmy.penup()      # Don't draw when moving forward.
        timmy.forward(50)  # Leave empty space of 50 units between 2 dots.
    timmy.setheading(90)   # Turn east.
    timmy.forward(50)      # Leave a gap of 50 spaces between 2 rows.
    timmy.setheading(180)  # Turn south.
    timmy.forward(500)     # Take the turtle to the position of 1st dot from previous row (10*50=500).
    timmy.setheading(0)    # Face north.

screen = t.Screen()
screen.exitonclick()
