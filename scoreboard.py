from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", False, align="center", font=("bold", 18, "normal"))


    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("bold", 18, "normal"))
