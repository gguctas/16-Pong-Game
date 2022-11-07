from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Gokay Pong")
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

screen.listen()
screen.onkey(r_paddle.yukari, "Up")
screen.onkey(r_paddle.asagi, "Down")
screen.onkey(l_paddle.yukari, "w")
screen.onkey(l_paddle.asagi, "s")


scoreboard = Scoreboard()

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision.
    if ball.ycor() > 280 or ball.ycor() < -280:
        #now have to bounce.
        ball.bounce_y()

    # Detect collision between paddle and ball.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect r_paddle miss shot
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l_paddle miss shot
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()