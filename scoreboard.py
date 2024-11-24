from turtle import Turtle  # Importing the Turtle class for creating and managing the scoreboard

# Constants for font and alignment properties
FONT = ("Courier", 24, "normal")  # Define font style, size, and type
ALIGNMENT = "left"  # Text alignment for the scoreboard

class Scoreboard(Turtle):
    """
    Scoreboard class inherits from Turtle and manages the game score and game over display.
    """

    def __init__(self):
        """
        Initialize the Scoreboard class.
        """
        super().__init__()  # Initialize the Turtle superclass
        self.color("black")  # Set the text color to black
        self.penup()  # Lift the pen to prevent drawing when moving the turtle
        self.goto(-290, 260)  # Position the scoreboard at the top-left corner of the screen
        self.hideturtle()  # Hide the turtle cursor for a cleaner display
        self.count = 0  # Initialize the level count to 0
        self.update_scoreboard()  # Display the initial scoreboard

    def update_scoreboard(self):
        """
        Update the scoreboard to display the current level.
        """
        self.clear()  # Clear the previous text from the screen
        self.write(f"Level:{self.count}", align=ALIGNMENT, font=FONT)  # Display the current level

    def game_over(self):
        """
        Display a "GAME OVER" message at the center of the screen.
        """
        self.penup()  # Ensure no lines are drawn
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)  # Display the "GAME OVER" message

    def update_level(self):
        """
        Increment the level count and update the scoreboard.
        """
        self.count += 1  # Increment the level count by 1
        self.update_scoreboard()  # Refresh the scoreboard to display the new level
