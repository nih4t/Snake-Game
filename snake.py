from turtle import Turtle

MOVE_DISTANCE = 20
SEGMENT_SIZE = 20
INITIAL_LENGTH = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """Create the initial snake with a specified number of segments."""
        for i in range(INITIAL_LENGTH):
            self.add_segment((-i * SEGMENT_SIZE, 0))

    def add_segment(self, position):
        """Add a new segment to the snake's body at the specified position."""
        segment = Turtle()
        segment.shape('square')
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.snake_body.append(segment)

    def extend(self):
        """Extend the snake by adding a new segment at the position of the last segment."""
        self.add_segment(self.snake_body[-1].position())

    def up(self):
        """Change the snake's direction to up if it's not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down if it's not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left if it's not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right if it's not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        """Move the snake forward by shifting each segment to the position of the segment ahead."""
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def set_snake_size(self, scale_factor):
        """Set the size of the snake segments by scaling their width and height."""
        if not (scale_factor[0] > 0 and scale_factor[1] > 0):
            raise ValueError("Scale factors must be positive numbers.")
        for segment in self.snake_body:
            segment.shapesize(stretch_wid=scale_factor[0], stretch_len=scale_factor[1])
