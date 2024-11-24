# Importing necessary modules and classes
import time  # Used to add delays in the game loop
from turtle import Screen  # Used to create and manage the game screen
from player import Player  # Player class to handle player character
from car_manager import CarManager  # CarManager class to manage cars
from scoreboard import Scoreboard  # Scoreboard class to display scores and game status

# Setting up the game screen
screen = Screen()  # Create a screen object
screen.setup(width=600, height=600)  # Set screen dimensions to 600x600 pixels
screen.tracer(0)  # Turn off automatic animation updates for smoother gameplay

# Initializing game objects
player = Player()  # Create a player object
car_manager = CarManager()  # Create a car manager object to handle car movement and creation
scoreboard = Scoreboard()  # Create a scoreboard object to track levels and game status

# Setting up keyboard controls
screen.listen()  # Enable screen to listen for keyboard input
screen.onkeypress(fun=player.move, key="Up")  # Bind the "Up" arrow key to the player's move method

# Main game loop
game_is_on = True  # Flag to keep the game running
while game_is_on:
    time.sleep(0.1)  # Add a short delay between iterations for smoother gameplay
    screen.update()  # Update the screen to reflect changes

    # Create new cars and move existing ones
    car_manager.create_car()  # Generate a new car at random intervals
    car_manager.move()  # Move all cars on the screen

    # Check for collision between player and cars
    for cars in car_manager.all_cars:  # Loop through all cars managed by car_manager
        if cars.distance(player) <= 20:  # Check if any car is close to the player
            scoreboard.game_over()  # Display game over message
            game_is_on = False  # End the game loop

    # Check if player successfully crosses to the other side
    if player.restart():  # Check if the player has reached the top and should restart
        scoreboard.update_level()  # Increase the level and update the scoreboard
        car_manager.increase_car_speed()  # Increase the speed of the cars for added difficulty

# Exit the game when the screen is clicked
screen.exitonclick()  # Wait for a click on the screen to close the game window
