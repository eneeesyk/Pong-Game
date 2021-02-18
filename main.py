from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game!")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0), 5, 1)
l_paddle = Paddle((-350, 0), 5, 1)
ball = Ball()
scoreboard = Scoreboard()

for pos in range(200, -800, -75):
    Paddle((0, 300 + pos), 2, 0.2)

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    """Detect collision with wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """Detect collision with paddles"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """Detect R paddle misses"""
    if ball.xcor() > 410:
        ball.reset_ball()
        scoreboard.l_point()
    """Detect L paddle misses"""
    if ball.xcor() < -410:
        ball.reset_ball()
        scoreboard.r_point()

    

screen.exitonclick()
