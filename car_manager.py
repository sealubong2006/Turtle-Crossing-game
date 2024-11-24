from turtle import Turtle  # Import the Turtle class for creating car objects
import random  # Import the random module for generating random values

# Constants for car properties and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of possible car colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars
MOVE_INCREMENT = 10  # The amount by which car speed increases after each level

class CarManager:
    """
    CarManager class handles the creation, movement, and speed management of cars.
    """

    def __init__(self):
        """
        Initialize the CarManager class.
        """
        super().__init__()  # Initialize the parent class (not strictly necessary here as no inheritance is used)
        self.all_cars = []  # List to store all car objects
        self.starting_move = STARTING_MOVE_DISTANCE  # Set the initial movement speed of the cars

    def create_car(self):
        """
        Randomly create a car with a 1 in 6 chance and add it to the list of cars.
        """
        random_chance = random.randint(1, 6)  # Generate a random number between 1 and 6
        if random_chance == 1:  # Only create a car if the random number is 1
            new_car = Turtle("square")  # Create a new car shaped as a rectangle
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the shape to look like a car
            new_car.penup()  # Lift the pen to avoid drawing lines
            new_car.color(random.choice(COLORS))  # Assign a random color to the car
            random_y = random.randint(-250, 250)  # Generate a random Y-coordinate within screen bounds
            new_car.goto(300, random_y)  # Position the car at the right edge of the screen with the random Y-coordinate
            self.all_cars.append(new_car)  # Add the new car to the list of cars

    def move(self):
        """
        Move all cars to the left by the current speed.
        """
        for cars in self.all_cars:  # Iterate over all car objects
            cars.backward(self.starting_move)  # Move each car backward by the current speed

    def increase_car_speed(self):
        """
        Increase the speed of the cars by the defined MOVE_INCREMENT.
        """
        self.starting_move += MOVE_INCREMENT  # Increase the speed by the increment value

    def return_original_speed(self):
        """
        Reset the speed of the cars to the initial value.
        """
        self.starting_move = STARTING_MOVE_DISTANCE  # Set the speed back to the starting value
