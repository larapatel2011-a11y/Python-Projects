import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()

t.shape("circle")
t.penup()
t.backward(300)
t.left(90)
t.pendown()

def semicircle():
    for i in range(17):
        t.forward(10)
        t.right(10)
    #t.circle(50,180)
    t.forward(20)
    t.setheading(90)

while True:
    t.color(random.random(), random.random(), random.random())
    semicircle()