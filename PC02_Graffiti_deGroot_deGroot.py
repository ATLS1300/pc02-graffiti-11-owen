#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

up()
goto(-23,90)
down()
circle(20)
up()
goto(40,100)
down()
circle(20)
up()
goto(-10,140)
down()
left(60)
forward(20)
left(60)
forward(20)
up()
goto(70,-71)
right(60)
pensize(10)
down()
forward(200)
up()
pensize(1)
goto(115,-200)
down()
left(30)
fillcolor("red")
begin_fill()
shape("square")
end_fill()


