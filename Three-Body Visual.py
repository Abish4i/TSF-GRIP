import turtle
import math
import tkinter as TP

def setup():
    global sun, planet1, planet2
    sun = turtle.Turtle()
    planet1 = turtle.Turtle()
    planet2 = turtle.Turtle()
    sun.shape("circle")
    planet1.shape("circle")
    planet2.shape("circle")
    sun.color("yellow")
    planet1.color("blue")
    planet2.color("green")
    sun.shapesize(5)
    planet1.shapesize(2)
    planet2.shapesize(2)
    sun.penup()
    planet1.penup()
    planet2.penup()
    sun.goto(0, 0)
    planet1.goto(-200, 0)
    planet2.goto(200, 0)

def move():
    global sun, planet1, planet2
    G = 0.1
    m1 = 10
    m2 = 10
    r1 = planet1.distance(sun)
    r2 = planet2.distance(sun)
    F1 = G * m1 * m2 / (r1 ** 2)
    F2 = G * m1 * m2 / (r2 ** 2)
    a1 = F1 / m1
    a2 = F2 / m2
    angle1 = planet1.towards(sun)
    angle2 = planet2.towards(sun)
    planet1.left(angle1 + 90)
    planet1.forward(a1)
    planet1.right(angle1 + 90)
    planet2.right(angle2 + 90)
    planet2.forward(a2)

setup()

while True:
    move()
    turtle.update()
