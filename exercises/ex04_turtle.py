"""EX04 - A House on a Sunny Day."""

__author__ = "730236204"

from turtle import Turtle, colormode, done
colormode(255)

"""Something interesting I did on this exercise was in the sun function's 
second loop I manipulated the side length variable to multiply by 1 to make 
complex line work that looks like a sun."""

MAX_SPEED: int = 0


def main() -> None:
    """The entrypoint of my scene."""
    # sky
    draw_sky(sky, -1000.0, 500.0)
    # ground
    draw_ground(ground, -1000.0, -115.0)
    # house
    draw_house(house, 23.0, 20.0)
    # roof
    draw_roof(roof, 10.0, 20.0)
    # windows
    draw_square(square, 80.0, -10.0, 70.0)
    draw_square(square, 200.0, -10.0, 70.0)
    # door
    draw_door(door, 103.0, -130.0)
    draw_square(square, 230.0, -210.0, 18.0)
    # cloud 1
    draw_square(square, -35.0, 250.0, 20.0)
    draw_square(square, -40.0, 255.0, 20.0)
    draw_square(square, -20.0, 245.0, 20.0)
    draw_square(square, -15.0, 250.0, 20.0)
    draw_square(square, -15.0, 256.0, 20.0)
    draw_square(square, -30.0, 260.0, 20.0)
    # cloud 2
    draw_square(square, -105.0, 290.0, 20.0)
    draw_square(square, -120.0, 298.0, 20.0)
    draw_square(square, -130.0, 295.0, 20.0)
    draw_square(square, -123.0, 280.0, 20.0)
    draw_square(square, -111.0, 277.0, 20.0)
    # cloud 3
    draw_square(square, -300.0, 295.0, 20.0)
    draw_square(square, -310.0, 290.0, 20.0)
    draw_square(square, -320.0, 298.0, 20.0)
    draw_square(square, -305.0, 305.0, 20.0)
    # cloud 4
    draw_square(square, 300.0, 285.0, 20.0)
    draw_square(square, 293.0, 290.0, 20.0)
    draw_square(square, 285.0, 286.0, 20.0)
    draw_square(square, 290.0, 280.0, 20.0)
    # cloud 5
    draw_square(square, 45.0, 305.0, 20.0)
    draw_square(square, 53.0, 310.0, 20.0)
    draw_square(square, 65.0, 306.0, 20.0)
    draw_square(square, 55.0, 300.0, 20.0)
    # sun
    draw_sun(sun, -320.0, -1.0)
    done()


sky: Turtle = Turtle()


def draw_sky(sky: Turtle, x: float, y: float) -> None:
    """Draws a square with given x and y to represent sky."""
    sky.penup()
    sky.goto(x, y) 
    sky.setheading(0.0)
    sky.fillcolor(100, 149, 237)
    sky.pencolor(100, 149, 237)
    sky.speed(MAX_SPEED)
    sky.pendown()
    i: int = 0
    sky.begin_fill()
    while i < 4:
        sky.forward(2000.0)
        sky.right(90)
        i = i + 1
    sky.hideturtle()
    sky.end_fill()


ground: Turtle = Turtle()


def draw_ground(ground: Turtle, x: float, y: float) -> None:
    """Draws a square with given x and y to represent ground."""
    ground.penup()
    ground.goto(x, y) 
    ground.setheading(0.0)
    ground.fillcolor(143, 188, 143)
    ground.pencolor(143, 188, 143)
    ground.speed(MAX_SPEED)
    ground.pendown()
    i: int = 0
    ground.begin_fill()
    while i < 4:
        ground.forward(2000.0)
        ground.right(90)
        i = i + 1
    ground.hideturtle()
    ground.end_fill()


house: Turtle = Turtle()


def draw_house(house: Turtle, x: float, y: float) -> None:
    """Draws the body of house whose top-left corner is located at x, y."""
    house.penup()
    house.goto(x, y) 
    house.setheading(0.0)
    house.fillcolor(100, 50, 60)
    house.pencolor(100, 50, 60)
    house.speed(MAX_SPEED)
    house.pendown()
    i: int = 0
    house.begin_fill()
    while i < 4:
        house.forward(300)
        house.right(90)
        i = i + 1
    house.hideturtle()
    house.end_fill()


roof: Turtle = Turtle()


def draw_roof(roof: Turtle, x: float, y: float) -> None:
    """Draws a triange with given x and y to represent roof."""
    roof.begin_fill()
    roof.fillcolor(128, 128, 128)
    roof.pencolor(128, 128, 128)
    roof.penup()
    roof.goto(x, y)
    roof.speed(MAX_SPEED)
    roof.pendown()
    i: int = 0
    while (i < 3):
        roof.forward(330.0)
        roof.left(120)
        i = i + 1   
    roof.hideturtle()
    roof.end_fill()


square: Turtle = Turtle()


def draw_square(square: Turtle, x: float, y: float, width: float) -> None:
    """Draws a square of the given width whose top-left corner is located at x, y."""
    square.penup()
    square.goto(x, y) 
    square.setheading(0.0)
    square.fillcolor(211, 211, 211)
    square.pencolor(211, 211, 211)
    square.speed(MAX_SPEED)
    square.pendown()
    i: int = 0
    square.begin_fill()
    while i < 4:
        square.forward(width)
        square.right(90)
        i = i + 1
    square.hideturtle()
    square.end_fill()


door: Turtle = Turtle()


def draw_door(door: Turtle, x: float, y: float) -> None:
    """Draws a square with given x and y to represent door."""
    door.penup()
    door.goto(x, y) 
    door.setheading(0.0)
    door.fillcolor(218, 165, 32)
    door.pencolor(218, 165, 32)
    door.speed(MAX_SPEED)
    door.pendown()
    i: int = 0
    door.begin_fill()
    while i < 4:
        door.forward(150.0)
        door.right(90)
        i = i + 1
    door.hideturtle()
    door.end_fill()


sun: Turtle = Turtle()


def draw_sun(sun: Turtle, x: float, y: float) -> None:
    """Draws repeating outlines of triangles with given x and y to represent sun."""
    sun.penup()
    sun.goto(x, y)
    sun.pencolor(255, 215, 0)
    sun.speed(MAX_SPEED)
    sun.pendown()
    i: int = 0
    while (i < 3):
        sun.forward(300)
        sun.left(120)
        i = i + 1
        side_length: float = 300
        a: int = 0
        while (a < 72):
            side_length = side_length * 1
            sun.forward(side_length)
            sun.left(130)
            a = a + 1
    sun.hideturtle()


if __name__ == "__main__":
    main()