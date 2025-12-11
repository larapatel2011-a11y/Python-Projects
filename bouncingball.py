import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
t.speed(1)
t.shape("circle")
t.penup()
t.left(90)
def move():
    turtle.colormode(255)
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    t.color(r,g,b)
    t.forward(150)
    t.backward(150)
while True:
    move()