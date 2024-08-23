from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        """Initialize the food object with specific shape, color, and speed, and place it randomly on the screen."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.70, stretch_len=0.70)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a random position on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
