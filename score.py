from turtle import Turtle

# Constants for alignment and font settings
ALLIGN = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        # Read the high score from a file
        with open("data.txt") as d:
            self.high_score = int(d.read())
        self.score = 0  # Initialize the current score
        self.color("white")  # Set the color of the scoreboard
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Prevent drawing lines when moving
        self.goto(0, 250)  # Position the scoreboard at the top of the screen
        self.upgrade()  # Initial display of score

    def upgrade(self):
        # Update the scoreboard display
        self.write(arg=f"SCORE {self.score} : HIGH SCORE {self.high_score}", align=ALLIGN, font=FONT)

    def increase(self):
        # Increase the current score and update the display
        self.score += 1
        self.clear()  # Clear the previous score display
        self.upgrade()  # Refresh the scoreboard display

    def highest_score(self):
        # Check if the current score exceeds the high score
        if self.high_score < self.score:
            self.high_score = self.score  # Update high score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # Save the new high score to the file
            self.score = 0  # Reset the current score
        else:
            self.score = 0  # Reset the current score if not a new high score
        self.clear()  # Clear the display
        self.write(arg=f"SCORE {self.score} : HIGH SCORE {self.high_score}", align=ALLIGN, font=FONT)  # Update display
