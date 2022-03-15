import turtle as t
import random

Running = True

screen = t.Screen()

screen.screensize(800, 800, "lightgreen")

position = [-280, -120, 25, 180, 340]
colors = ["purple", "brown", "orange", "blue", "red"]
turtles = []
bet = screen.textinput("TURTLE RACE", "Place your bet! (purple, brown, orange, blue, red): ")

for index in range(0, 5):
    tim = t.Turtle()
    tim.shape("turtle")
    tim.shapesize(1.5)
    tim.speed("fast")
    tim.penup()
    tim.goto(x=-450, y=position[index])
    tim.color(colors[index])
    turtles.append(tim)

while Running:
    for turtle in turtles:
        if turtle.xcor() > 425:
            Running = False
            winner = turtle.pencolor()
            if winner == bet:
                result = screen.textinput("WIN", f"You won! {winner} is the right answer! Congrtulations!")
            else:
                result = screen.textinput("LOST", f"You lost! {winner} was the right answer")
            random_speed = random.randint(0, 20)
            turtle.forward(random_speed)

screen.exitonclick()
