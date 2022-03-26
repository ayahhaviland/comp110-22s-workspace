from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-120, -60)
leo.pendown()

leo.speed(50)
leo.hideturtle()

colormode(255)
leo.pencolor("beige")
leo.fillcolor("light green")

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()

bob.penup()
bob.goto(-120, -60)
bob.pencolor("forest green")
bob.pendown()

bob.speed(100)

i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i = i + 1

i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i = i + 1
    side_length: float = 300
    x: int = 0
    while (x < 80):
        side_length = side_length * 1
        bob.forward(side_length)
        bob.left(130)
        x = x + 1
bob.hideturtle()

done()