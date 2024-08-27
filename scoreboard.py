from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard with default settings and display the initial score."""
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update()

    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1

        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update()

    # def game_over(self):
    #     """Display 'GAME OVER' at the center of the screen."""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align="center", font=("Arial", 16, "normal"))

    def update(self):
        """Update the scoreboard display with the current score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Arial", 18, "normal"))
