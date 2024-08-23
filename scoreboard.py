from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard with default settings and display the initial score."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update()

    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        """Display 'GAME OVER' at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 16, "normal"))

    def update(self):
        """Update the scoreboard display with the current score."""
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 18, "normal"))
