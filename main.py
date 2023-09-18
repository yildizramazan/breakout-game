from turtle import Turtle, Screen
import random
screen = Screen()
screen.title("My Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

bricks_list = []

def create_bricks():
    colors = ["red", "orange", "yellow", "green", "blue"]
    brick_goto_y = 250
    for y in range(5):
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

def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



while True:
    screen.update()
    move_ball()





