import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)

position = [-260, -130, 0, 130, 260]
colors = ["purple", "brown", "orange", "blue", "red"]
turtles = []
bet = screen.textinput("TURTLE RACE", "Place your bet! (purple, brown, orange, blue, red): ")

for index in range(0, 5):
    tim = Turtle()
    tim.shape("turtle")
    tim.shapesize(1.5)
    tim.speed("fast")
    tim.penup()
    tim.goto(x=-350, y=position[index])
    tim.color(colors[index])
    turtles.append(tim)

is_on = True

while is_on:
    for turtle in turtles:
        if turtle.xcor() >= 360:
            is_on = False
            winner = turtle.pencolor()
            if winner == bet:
                turtle.write(f"You won, {winner} turtle is winner.", move=False, align="right", font=("Arial", 20, "normal"))
            else:
                turtle.write(f"You lost, {winner} turtle is winner.", move=False, align="right", font=("Arial", 20, "normal"))
        random_speed = random.randint(1, 20)
        turtle.forward(random_speed)

screen.exitonclick()
