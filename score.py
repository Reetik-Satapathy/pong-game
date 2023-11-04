from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 270)
        self.write(self.l_score, False, "center", 30)
        self.goto(100, 270)
        self.write(self.r_score, False, "center", 30)

    def left_score(self):
        self.l_score += 1
        self.update()

    def right_score(self):
        self.r_score += 1
        self.update()
