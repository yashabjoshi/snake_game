from turtle import Turtle

# Constants for movement directions and starting positions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments

class Snake:
    def __init__(self):
        self.snake_list = []  # List to hold the snake segments
        self.create_snake()  # Create the initial snake
        self.head = self.snake_list[0]  # The head of the snake is the first segment

    def create_snake(self):
        # Create the initial snake segments based on starting positions
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        # Add a new segment to the snake at the specified position
        segment = Turtle("square")  # Create a new square segment
        segment.penup()  # Prevent the segment from drawing lines when moving
        segment.color("white")  # Set the color of the segment
        segment.goto(position)  # Move the segment to its starting position
        self.snake_list.append(segment)  # Add the segment to the snake list

    def extend_snake(self):
        # Extend the snake by adding a new segment at the position of the last segment
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        # Move the snake by updating the position of each segment
        for tale in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[tale - 1].xcor()  # Get the x-coordinate of the segment in front
            new_y = self.snake_list[tale - 1].ycor()  # Get the y-coordinate of the segment in front
            self.snake_list[tale].goto(new_x, new_y)  # Move the current segment to that position
        self.head.forward(20)  # Move the head forward by 20 units

    def reset(self):
        # Reset the snake to its starting position
        for snakes in self.snake_list:
            snakes.goto(1000, 1000)  # Move all segments off the screen
        self.snake_list.clear()  # Clear the snake list
        self.create_snake()  # Create a new snake
        self.head = self.snake_list[0]  # Reset the head to the new snake's head

    def up(self):
        # Change the direction of the snake to up if it is not already going down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the direction of the snake to down if it is not already going up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # Change the direction of the snake to right if it is not already going left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # Change the direction of the snake to left if it is not already going right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
