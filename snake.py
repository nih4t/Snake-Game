from turtle import Turtle

MOVE_DISTANCE = 20
SEGMENT_SIZE = 20
DEFAULT_SIZE = 20  # pixels
INITIAL_LENGTH = 3  # Initial number of segments

class Snake:
    def __init__(self):
        self.snake_body = []  # list of body segments
        self.create_snake()

    def create_snake(self):
        """Initialize the snake with a default number of segments."""
        for i in range(INITIAL_LENGTH):
            self.add_segment((-i * SEGMENT_SIZE, 0))

    def add_segment(self, position):
        """Create a new segment and add it to the snake's body."""
        segment = Turtle()
        segment.shape('square')
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.snake_body.append(segment)

    def move(self):
        """Move the snake forward by shifting each segment to the position of the previous one."""
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def set_snake_size(self, scale_factor):
        """
        Set the size of the snake segments by scaling their width and height.

        :param scale_factor: A tuple (width_scale, height_scale) to set the new size.
        :raises ValueError: If scale_factor values are not positive.
        """
        if not (scale_factor[0] > 0 and scale_factor[1] > 0):
            raise ValueError("Scale factors must be positive numbers.")
        for segment in self.snake_body:
            segment.shapesize(stretch_wid=scale_factor[0], stretch_len=scale_factor[1])





