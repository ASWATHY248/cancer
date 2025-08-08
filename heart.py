import turtle

# Set up turtle screen
t = turtle.Turtle()
t.fillcolor('red')
t.begin_fill()

# Draw heart shape
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)

t.end_fill()
t.hideturtle()
turtle.done()