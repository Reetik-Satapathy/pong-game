from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(0.8, 0.8)
        self.xpos = 5
        self.ypos = 5
        self.move_speed = 0.02

    def move_ball(self):
        xcor = self.xcor() + self.xpos
        ycor = self.ycor() + self.ypos
        self.goto(xcor, ycor)

    def bounce_wall(self):
        self.ypos *= -1

    def bounce_paddle(self):
        self.xpos *= -1

    def reset(self):
        self.home()
        self.xpos *= -1

    def inc_speed(self):
        self.move_speed *= 0.99
