# Pumpkin Drawing
# Author: Cadee
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Carve the left eye
carver.penup()
carver.setposition(-40, 15)
carver.pensize(30)
carver.pendown()
carver.forward(7)
carver.pensize(15)

# Carve the right eye
carver.penup()
carver.setposition(40, 15)
carver.pensize(30)
carver.pendown()
carver.forward(7)
carver.pensize(15)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

# Mouth
carver.penup()
carver.setposition(-45, -30)
carver.pensize(38)
carver.pendown()
carver.forward(85)
carver.pensize(18)

turtle.done()
