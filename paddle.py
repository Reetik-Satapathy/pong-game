from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.penup()
        self.turtlesize(5, 1)
        self.goto(position)

    def go_up(self):
        xcor = self.xcor()
        ycor = self.ycor() + 20
        self.goto(xcor, ycor)

    def go_down(self):
        xcor = self.xcor()
        ycor = self.ycor() - 20
        self.goto(xcor, ycor)
