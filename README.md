# Turtle Crossing Game

## Description
This is a fun Python game where the player controls a turtle trying to cross a busy road filled with cars. The game gets harder as you progress by increasing the speed of the cars with every level.

## How to Play
1. Use the **Up arrow key** to move the turtle forward.
2. Avoid the moving cars! If the turtle collides with a car, the game is over.
3. Reach the top of the screen to complete a level. Each level increases the difficulty by making the cars move faster.

## Features
- **Player movement**: Control the turtle's movement using the `Up` arrow key.
- **Random cars**: Cars are generated randomly with different colors and move from right to left.
- **Scoreboard**: Displays your current level at the top-left corner of the screen.
- **Game Over screen**: Displays a "GAME OVER" message if the turtle collides with a car.

## Project Structure
The project is divided into multiple Python files for modularity:
1. **`main.py`**: The main game logic that combines all the other components.
2. **`player.py`**: Manages the player's turtle movement and checks if the player crosses the finish line.
3. **`car_manager.py`**: Handles the creation, movement, and speed of the cars.
4. **`scoreboard.py`**: Manages the display of the current level and the "GAME OVER" message.

## Requirements
- Python 3.x
- Turtle module (built into Python)

## How to Run the Game
1. Make sure all files (`main.py`, `player.py`, `car_manager.py`, and `scoreboard.py`) are in the same folder.
2. Open a terminal or IDE and run the following command:
   ```bash
   python main.py
   ```
3. Enjoy the game!

## Future Improvements
- Add more levels with different challenges.
- Add a feature to restart the game without closing the window.
- Add sound effects when the player wins or loses.
