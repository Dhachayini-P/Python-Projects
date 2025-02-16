import tkinter as tk
import random

# Initialize the window
window = tk.Tk()
window.title("Snake Game")

# Set the width and height of the game
width = 600
height = 400

# Create the game canvas
canvas = tk.Canvas(window, width=width, height=height, bg='black')
canvas.pack()

# Initialize game variables
snake = [(100, 100), (90, 100), (80, 100)]  # List of snake positions (x, y)
snake_direction = 'Right'  # Initial direction
food = None
game_over = False
score = 0

# Display score
score_label = tk.Label(window, text="Score: 0", font=("Arial", 14))
score_label.pack()

# Bind keys to control snake
def change_direction(event):
    global snake_direction
    if event.keysym == "Left" and snake_direction != 'Right':
        snake_direction = 'Left'
    elif event.keysym == "Right" and snake_direction != 'Left':
        snake_direction = 'Right'
    elif event.keysym == "Up" and snake_direction != 'Down':
        snake_direction = 'Up'
    elif event.keysym == "Down" and snake_direction != 'Up':
        snake_direction = 'Down'

window.bind("<Left>", change_direction)
window.bind("<Right>", change_direction)
window.bind("<Up>", change_direction)
window.bind("<Down>", change_direction)

# Function to create food at a random position
def create_food():
    global food
    food_x = random.randint(0, (width // 10) - 1) * 10
    food_y = random.randint(0, (height // 10) - 1) * 10
    food = (food_x, food_y)
    canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill="red", outline="red")

# Function to update the canvas with snake and food
def update_canvas():
    global snake, food
    canvas.delete("all")  # Clear the canvas

    # Draw the snake
    for segment in snake:
        x, y = segment
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", outline="green")

    # Draw the food
    food_x, food_y = food
    canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill="red", outline="red")

# Function to move the snake
def move_snake():
    global snake, snake_direction, food, game_over, score

    if game_over:
        canvas.create_text(width // 2, height // 2, text="Game Over", fill="white", font=("Arial", 24))
        return

    # Get the current head position
    head_x, head_y = snake[0]

    # Move the head in the current direction
    if snake_direction == 'Left':
        head_x -= 10
    elif snake_direction == 'Right':
        head_x += 10
    elif snake_direction == 'Up':
        head_y -= 10
    elif snake_direction == 'Down':
        head_y += 10

    # New head position
    new_head = (head_x, head_y)

    # Check if snake has collided with the boundaries or itself
    if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height or new_head in snake[1:]:
        game_over = True
        canvas.create_text(width // 2, height // 2, text="Game Over", fill="white", font=("Arial", 24))
        return

    # Check if snake has eaten the food
    if new_head == food:
        snake.append(snake[-1])  # Add a new segment to the snake
        score += 10
        score_label.config(text=f"Score: {score}")
        create_food()

    # Move the snake by updating its position
    snake = [new_head] + snake[:-1]

    update_canvas()
    window.after(100, move_snake)

# Initialize the game by creating food and moving the snake
create_food()
move_snake()

# Start the game
window.mainloop()
