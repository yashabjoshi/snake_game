from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Prevent the food from drawing a line when moving
        self.color("blue")  # Set the color of the food
        self.shapesize(stretch_wid=0.80, stretch_len=0.80)  # Adjust the size of the food
        self.new()  # Position the food at a random location

    def new(self):
        # Generate random x and y coordinates within the specified range
        xd = random.randint(-280, 260)
        yd = random.randint(-280, 280)
        self.goto(xd, yd)  # Move the food to the new random position
