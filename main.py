from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from score import Score

# screen setup
screen = Screen()
screen.bgcolor("green")
screen.setup(800, 600)
screen.tracer(0)
score = Score()

# paddle setup
l_pad = Paddle((-380, 0))
r_pad = Paddle((380, 0))

# control the paddle
screen.listen()
# left paddle
screen.onkeypress(r_pad.go_up, "Up")
screen.onkeypress(r_pad.go_down, "Down")
# right paddle
screen.onkeypress(l_pad.go_up, "w")
screen.onkeypress(l_pad.go_down, "s")

# ball setup
ball = Ball()

# screen update
flag = True
while flag:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # bounce mechanism with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # bounce mechanism with paddles
    if (ball.distance(r_pad) < 40 and ball.xcor() > 330) or (ball.distance(l_pad) < 40 and ball.xcor() < -330):
        ball.bounce_paddle()
        ball.inc_speed()

    # if ball misses the paddle, keeping score and updating ball speed upon collision with paddle
    if ball.xcor() > 400 or ball.xcor() < -400:
        time.sleep(2)
        if ball.xcor() > 400:
            score.left_score()
        else:
            score.right_score()
        ball.reset()
        ball.move_speed = 0.02

screen.exitonclick()
