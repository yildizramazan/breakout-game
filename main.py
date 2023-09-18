from turtle import Turtle, Screen
import random
import time

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


screen = Screen()
screen.title("My Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

score_count = 0
score = Turtle()
score.penup()
score.hideturtle()
score.goto(0,-285)
score.pencolor("white")
score.write(f"Score: {score_count} ", font=FONT, align=ALIGNMENT)



number_of_lose = 0

hearts = []
def create_hearts(number):
    heart_goto_x = -30
    for _ in range(number):
        heart = Turtle()
        heart.penup()
        heart.color("brown")
        heart.shape("circle")
        heart.goto(heart_goto_x, 280)
        heart_goto_x += 30
        hearts.append(heart)

create_hearts(3)

bricks_list = []
def create_bricks():
    global brick
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    brick_goto_y = 250
    for y in range(6):
        brick_goto_x = -275
        color = colors[y]
        for x in range(10):
            brick = Turtle()
            brick.speed(0)
            brick.shape("square")
            brick.color(color)
            brick.penup()
            brick.goto(brick_goto_x, brick_goto_y)
            bricks_list.append(brick)
            brick_goto_x += 60
        brick_goto_y -= 30

create_bricks()


paddle = Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

ball = Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

def paddle_right():
    x = paddle.xcor()
    if x < 340:
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -340:
        x -= 20
    paddle.setx(x)

screen.listen()
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "Left")

def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


def check_collisions():
    global score_count
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    if (-240 > ball.ycor() > -250) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240)
        ball.dy *= -1

    for brick in bricks_list:
        if ball.distance(brick) < 25:
            brick.goto(1000, 1000)
            bricks_list.remove(brick)
            ball.dy *= -1
            score_count += 1


while True:
    screen.update()
    move_ball()
    check_collisions()
    score.clear()
    score.write(f"Score: {score_count} ", font=FONT, align=ALIGNMENT)

    if ball.ycor() < -280:
        number_of_lose += 1
        if number_of_lose == 3:
            for brick in bricks_list:
                brick.goto(1000, 1000)
                brick.hideturtle()
            bricks_list = []
            create_bricks()
            number_of_lose = 0
            create_hearts(4)
            score_count = 0
        hearts[-1].goto(1000, 1000)
        hearts.pop()

    if ball.ycor() < -280 or len(bricks_list) == 0:
        ball.goto(0, 0)
        ball.dx = 2 * random.choice([-1, 1])
        ball.dy = -2
        score.clear()
        score.write(f"Score: {score_count} ", font=FONT, align=ALIGNMENT)




