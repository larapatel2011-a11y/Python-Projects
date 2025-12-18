import turtle
t= turtle.Turtle()
s= turtle.Screen()
t.shape("turtle")

maze=[
    "XXXXXXXXXXXXXXX",
    "X             X",
    "XXXXXXXXX XXXXX",
    "XX        XXXXX",
    "XX XX XXX XXXXX",
    "XX XX XXX    XX",
    "XX  X XXXXXX  X",
    "XXX X   XXXXX X",
    "XXX XXX XXXXX X",
    "X             X",
    "X             X",
    "X             X",
    "X             X",
    "X             X",
    "XXXXXXXXXXXXXXX"
]

for y in range (len(maze)):
    for x in range (len(maze[0])):
        turtlex = -288+(x*24)
        turtley = 288-(y*24)
        if maze[y][x] == "X":
            wall= turtle.Turtle()
            wall.shape("square")
            wall.color("blue")
            wall.penup()
            wall.speed(100)
            wall.goto(turtlex,turtley)


def right():
    xposition = t.xcor()+24
    t.setx (xposition)

s.listen()
s.onkey(right,"Right")









s.mainloop()



