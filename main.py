from turtle import Screen
from snake import Snake
from food import Food
import time
from score import ScoreBoard

# Initialize the game state
game_on = True

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the screen
screen.title("My Snake Game")  # Set the title of the window
screen.bgcolor("black")  # Set the background color of the screen
screen.tracer(0)  # Disable automatic screen updates for smoother animations

# Create game objects
snake = Snake()  # Initialize the snake
food1 = Food()  # Initialize the food
score1 = ScoreBoard()  # Initialize the scoreboard

# Listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")  # Bind the Up arrow key to the snake's upward movement
screen.onkey(snake.down, "Down")  # Bind the Down arrow key
screen.onkey(snake.right, "Right")  # Bind the Right arrow key
screen.onkey(snake.left, "Left")  # Bind the Left arrow key

# Main game loop
while game_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Control the game speed
    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food1) < 15:
        snake.extend_snake()  # Grow the snake
        food1.new()  # Create a new piece of food
        score1.increase()  # Increase the score

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        score1.highest_score()  # Update the highest score if applicable
        snake.reset()  # Reset the snake to its starting position

    # Detect collision with itself
    for segment in snake.snake_list[1:]:  # Check all segments of the snake
        if snake.head.distance(segment) < 10:  # If head collides with any segment
            score1.highest_score()  # Update the highest score if applicable
            snake.reset()  # Reset the snake to its starting position

# Exit the game on click
screen.exitonclick()
