import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(1)
t.color("black", "pink")  # Outline color, Fill color

# Start filling the heart
t.begin_fill()

# Draw the heart shape
t.penup()
t.goto(0, -100)
t.pendown()
t.left(140)
t.forward(224)
t.circle(-112, 200)
t.left(120)
t.circle(-112, 200)
t.forward(224)

# End filling
t.end_fill()

# Add custom message
t.penup()
t.goto(0, -20)
t.color("white")
t.write("LOVE", align="center", font=("Arial", 24, "bold"))