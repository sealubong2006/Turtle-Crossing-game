from turtle import Turtle  # Importing the Turtle class from the turtle module

# Constants for player properties and movement
STARTING_POSITION = (0, -280)  # The initial position of the player at the bottom center of the screen
MOVE_DISTANCE = 10  # The distance the player moves with each step
FINISH_LINE_Y = 280  # The Y-coordinate of the finish line at the top of the screen


class Player(Turtle):
    """
    Player class inherits from Turtle and represents the player character.
    """

    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.shape("turtle")  # Set the player's shape to a turtle
        self.color("black")  # Set the player's color to black
        self.setheading(90)  # Point the turtle upwards (90 degrees)
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.goto(STARTING_POSITION)  # Move the player to the starting position

    def move(self):
        """
        Move the player forward by the defined MOVE_DISTANCE.
        """
        self.forward(MOVE_DISTANCE)

    def restart(self):
        """
        Check if the player has reached the finish line.
        If true, reset the player's position and return True.
        """
        if self.ycor() >= FINISH_LINE_Y:  # Check if the player's Y-coordinate is at or above the finish line
            self.goto(STARTING_POSITION)  # Reset the player's position to the starting point
            return True  # Indicate that the player has successfully crossed the finish line
