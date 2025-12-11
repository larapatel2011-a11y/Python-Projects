import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
t.speed(70)
t.shape("circle")
t.penup()

while True:
    t.right(10)
    t.forward(10)
    turtle.colormode(255)
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    t.color(r,g,b)
