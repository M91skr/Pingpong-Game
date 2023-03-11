from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, font=("Courier", 60, "normal"))

    def update_l_score(self):
        self.l_score += 1
        self.update_scores()

    def update_r_score(self):
        self.r_score += 1
        self.update_scores()
