from turtle import Turtle, Screen


def borders(size, second_size):
    border = Turtle()
    Screen().bgcolor("black")
    border.goto(-470, -390)
    border.color("white")
    border.speed("fastest")
    for _ in range(4):

        if _ % 2 == 0:
            border.forward(size)
            border.left(90)

        else:
            border.forward(second_size)
            border.left(90)
    border.hideturtle()


def game():
    score_a = 0
    score_b = 0

    # screen settings
    screen = Screen()
    screen.title("Ping Pong")
    screen.bgcolor("black")
    screen.setup(width=1200, height=800)
    screen.tracer(0)

    # first racket
    racket_1 = Turtle()
    racket_1.speed(0)
    racket_1.shape("square")
    racket_1.color("white")
    racket_1.shapesize(stretch_wid=6, stretch_len=0.5)
    racket_1.penup()
    racket_1.goto(-450, 0)

    # second racket
    racket_2 = Turtle()
    racket_2.speed(0)
    racket_2.shape("square")
    racket_2.color("white")
    racket_2.shapesize(stretch_wid=6, stretch_len=0.5)
    racket_2.penup()
    racket_2.goto(450, 0)

    # ping pong ball
    ball = Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.ox = 0.5
    ball.oy = -0.5

    # pencil, to write on screen
    pencil = Turtle()
    pencil.speed(0)
    pencil.color("white")
    pencil.penup()
    pencil.goto(0, 300)
    pencil.hideturtle()
    pencil.write("Player A: 0  Player B: 0", align="center", font=("Arial", 20, "normal"))

    border = Turtle()
    border.color("white")

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
        if ball.xcor() > 460:
            ball.goto(0, 0)
            ball.oy *= -1
            score_a += 1
            pencil.clear()
            pencil.write("Player A : {}    Player B: {}".format(score_a, score_b), align="center",
                         font=("Arial", 20, "normal"))

        # racket_2 score earning and outputting
        if ball.xcor() < -460:
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

        if score_a >= 1:
            restart = screen.textinput("Game result", "Well done Player A you won ! \nDo you want to restart ? (y/n)")
            if restart == "y":
                screen.reset()
                borders(940, 665)
                game()
            else:
                break
        if score_b >= 1:
            restart = screen.textinput("Game result", "Well done Player B you won ! \nDo you want to restart ? (y/n)")
            if restart == "y":
                screen.reset()
                borders(940, 665)
                game()
            else:
                break


borders(940, 665)
game()
