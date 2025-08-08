import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")
t.color("magenta", "pink")  # Outline color, fill color

for i in range(36):
    t.begin_fill()
    for j in range(2):
        t.circle(100, 60)
        t.left(120)
    t.end_fill()
    t.left(10)

t.hideturtle()
turtle.done()