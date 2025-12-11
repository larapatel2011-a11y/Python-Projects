import turtle
import random
import time
t = turtle.Turtle()
s = turtle.Screen()

turtle.colormode(255)
def drawcircle():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    t.speed(100)
    t.color(r,g,b)
    t.begin_fill()
    t.circle(random.randint(10,100))
    t.end_fill()
    time.sleep(0.5)
    t.penup()
    t.goto(random.randint(-200,200),random.randint(-200,200))
    t.pendown()
for i in range(10):
    t.clear()
    drawcircle()







s.mainloop()
