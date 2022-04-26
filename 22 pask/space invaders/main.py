import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("space.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

borders = turtle.Turtle()
borders.speed(0)
borders.color("white")
borders.penup()
borders.setposition(-400, -250)
borders.pendown()
borders.pensize(3)

for _ in range(4):
    if _ % 2 == 0:
        borders.forward(800)
        borders.left(90)
    else:
        borders.forward(500)
        borders.left(90)
    borders.hideturtle()

score = 0

score_t = turtle.Turtle()
score_t.speed(0)
score_t.color("white")
score_t.penup()
score_t.setposition(-400, 260)
score_str = "Score: %s" % score
score_t.write(score_str, False, align="left", font=("Arial", 20, "normal"))
score_t.hideturtle()

player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -220)
player.setheading(90)

player_speed = 30
invaders_number = 5
invaders = []

for i in range(invaders_number):
    invaders.append(turtle.Turtle())

for invader in invaders:
    invader.shape("invader.gif")
    invader.penup()
    invader.speed(0)
    x = random.randint(-370, 370)
    y = random.randint(150, 220)
    invader.setposition(x, y)

invader_speed = 5

bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 30
bullet_state = "ready"


def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -370:
        x = -370
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 370:
        x = 370
    player.setx(x)


def fire_ammo():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def bullet_collision_w_invader(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 25:
        return True
    else:
        return False


def player_collision_w_invader(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 30:
        return True
    else:
        return False


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_ammo, "space")

Game_Over = False
missed_invaders = 0

while True:
    for invader in invaders:
        x = invader.xcor()
        x += invader_speed
        invader.setx(x)

        if invader.xcor() > 370:
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
                if i.ycor() < -220 and Game_Over is False:
                    i.hideturtle()
                    missed_invaders += 1
                    if missed_invaders == 10:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(150, 230)
                    i.setposition(x, y)
                    i.showturtle()
            invader_speed *= -1

        if invader.xcor() < -370:
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
                if i.ycor() < -220:
                    i.hideturtle()
                    missed_invaders += 1
                    if missed_invaders == 1:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 230)
                    i.setposition(x, y)
                    i.showturtle()
            invader_speed *= -1

        if bullet_collision_w_invader(bullet, invader):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 230)
            invader.setposition(x, y)
            score += 10
            score_str = "Score: %s" % score
            score_t.clear()
            score_t.write(score_str, False, align="left", font=("Arial", 20, "normal"))
            invader_speed += 0.5

        if player_collision_w_invader(player, invader):
            Game_Over = True

        if Game_Over is True:
            player.hideturtle()
            bullet.hideturtle()
            for i in invaders:
                i.hideturtle()
            screen.bgpic("game_over.gif")
            break

    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    if bullet.ycor() > 260:
        bullet.hideturtle()
        bullet_state = "ready"
