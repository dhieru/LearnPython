import turtle


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(1)
    draw_square(brad)
    draw_triangle(brad)
    window.exitonclick()


def draw_square(brad):
    count = 0
    while count < 4:
        brad.forward(100)
        brad.right(90)
        count += 1


def draw_triangle(brad):
    count = 0
    while count < 3:
        brad.forward(100)
        brad.left(120)
        count += 1


draw_art()