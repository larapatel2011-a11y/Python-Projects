import turtle
import time
t= turtle.Turtle()
s= turtle.Screen()
t.shape("turtle")

t.penup()
t.goto(-264,264)

maze=[
    "XXXXXXXXXXXXXXX",
    "X             X",
    "XXXXXXXXX XXXXX",
    "XX        XXXXX",
    "XX XX XXX XXXXX",
    "XX XX XXX    XX",
    "XX  X XXXXXX  X",
    "XXX X   XXXXX X",
    "XXX XXX XXXXXFX",
    "XXX X   XXXXX X",
    "XXX XXXXXXXX  X",
    "XXX        XXXX",
    "XXXXXXXXXX    X",
    "XXXXXXXXXXX XXX",
    "XXXXXXXXXXXXXXX"
]

walls = []

for y in range (len(maze)):
    for x in range (len(maze[0])):
        turtlex = -288+(x*24)
        turtley = 288-(y*24)
        if maze[y][x] == "X":
            wall= turtle.Turtle()
            walls.append(wall)
            wall.shape("square")
            wall.color("blue")
            wall.penup()
            wall.speed(100)
            wall.goto(turtlex,turtley)
        if maze[y][x] == "F":
            food = turtle.Turtle()
            food.shape("circle")
            food.color("red")
            food.penup()
            food.goto(turtlex,turtley)

def check(x,y):
    for wall in walls:
       if  wall.xcor() == x and wall.ycor() == y :
           return False
    return True

def right():
    xposition = t.xcor()+24
    if check(xposition, t.ycor()):
        t.setx (xposition)

def left():
    xposition = t.xcor()-24
    if check(xposition, t.ycor()):
        t.setx (xposition)

def up():
    yposition = t.ycor()+24
    if check(t.xcor(), yposition):
        t.sety (yposition)

def down():
    yposition = t.ycor()-24
    if check(t.xcor(), yposition):
        t.sety (yposition)

s.listen()
s.onkey(right,"Right")
s.onkey(left, "Left")
s.onkey(up, "Up" )
s.onkey(down, "Down")


while True:
    if t.distance(food)==0:
        t.write("Congratulations, you found the food")
    time.sleep(1)




s.mainloop()



