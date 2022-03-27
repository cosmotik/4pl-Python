import turtle

score_a = 0
score_b = 0

# screen settings
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.tracer(0)

# first racket
racket_1 = turtle.Turtle()
racket_1.speed(0)
racket_1.shape("square")
racket_1.color("white")
racket_1.shapesize(stretch_wid=6, stretch_len=0.5)
racket_1.penup()
racket_1.goto(-450, 0)

# second racket
racket_2 = turtle.Turtle()
racket_2.speed(0)
racket_2.shape("square")
racket_2.color("white")
racket_2.shapesize(stretch_wid=6, stretch_len=0.5)
racket_2.penup()
racket_2.goto(450, 0)

# ping pong ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.ox = 0.2
ball.oy = -0.2

# pne, to write on screen
pencil = turtle.Turtle()
pencil.speed(0)
pencil.color("white")
pencil.penup()
pencil.hideturtle()
pencil.goto(0, 300)
pencil.write("Player A: 0  Player B: 0", align="center", font=("Arial", 20, "normal"))


# key up/down functions
def racket_1_up():
    y = racket_1.ycor()
    y += 30
    racket_1.sety(y)


def racket_1_down():
    y = racket_1.ycor()
    y -= 30
    racket_1.sety(y)


def racket_2_up():
    y = racket_2.ycor()
    y += 30
    racket_2.sety(y)


def racket_2_down():
    y = racket_2.ycor()
    y -= 30
    racket_2.sety(y)


# press keys
screen.listen()
screen.onkey(racket_1_up, "w")
screen.onkey(racket_1_down, "s")
screen.onkey(racket_2_up, "Up")
screen.onkey(racket_2_down, "Down")

# game logic
while True:
    screen.update()

    # move the ball
    ball.setx(ball.xcor() + ball.ox)
    ball.sety(ball.ycor() + ball.oy)

    # border checking
    if ball.ycor() > 265:
        ball.sety(265)
        ball.oy *= -1

    if ball.ycor() < -380:
        ball.sety(-380)
        ball.oy *= -1

    # racket_1 score earning and outputting
    if ball.xcor() > 450:
        ball.goto(0, 0)
        ball.oy *= -1
        score_a += 1
        pencil.clear()
        pencil.write("Player A : {}    Player B: {}".format(score_a, score_b), align="center",
                     font=("Arial", 20, "normal"))

    # racket_2 score earning and outputting
    if ball.xcor() < -450:
        ball.goto(0, 0)
        ball.oy *= -1
        score_b += 1
        pencil.clear()
        pencil.write("Player A : {}    Player B: {}".format(score_a, score_b), align="center",
                     font=("Arial", 20, "normal"))

    # dont let rackets to go out of the board
    if racket_1.ycor() >= 245:
        racket_1.goto(-450, 245)
    if racket_1.ycor() <= -340:
        racket_1.goto(-450, -340)
    if racket_2.ycor() >= 245:
        racket_2.goto(450, 245)
    if racket_2.ycor() <= -340:
        racket_2.goto(450, -340)

    # ball colissions with racket_1 and racket_2
    if (ball.xcor() < -440 and ball.xcor() > -450) and (
            ball.ycor() < racket_1.ycor() + 50 and ball.ycor() > racket_1.ycor() - 50):
        ball.setx(-430)
        ball.ox *= -1

    if (ball.xcor() > 440 and ball.xcor() < 450) and (
            ball.ycor() < racket_2.ycor() + 50 and ball.ycor() > racket_2.ycor() - 50):
        ball.setx(430)
        ball.ox *= -1
