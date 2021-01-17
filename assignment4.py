# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:10:27 2021

@author: Swapnil Sirsat
"""

import turtle
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("white")
skk.write("B",move = False)
skk.forward(700)
skk.write("C",move = False)
skk.left(150)
skk.forward(800)
skk.penup()
skk.goto(0,0)
skk.setheading(0)
skk.pendown()
skk.left(45)
skk.forward(800)
turtle.done()
turtle.bye()