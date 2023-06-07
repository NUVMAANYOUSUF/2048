# 2048 Game

This is a simple implementation of the popular game 2048 using Pygame library. The game is played on a grid, where the player combines tiles with the same number to create higher-value tiles. The goal is to reach the 2048 tile.

# Requirements

To run the game, you need to have Python installed on your system. Additionally, you need to install the Pygame library. You can install Pygame using pip:
```shell
pip install pygame
```
# How to Play

   Run the 2048_game.py script using Python.
   Use the arrow keys (Up, Down, Left, Right) to move the tiles in the corresponding direction.
   Tiles with the same number will merge when they collide.
   After each move, a new tile with a value of 2 or 4 will appear on the grid.
   The game ends when there are no more possible moves or when you reach the 2048 tile.
   
 # Controls

   Arrow Up: Move tiles upwards
   Arrow Down: Move tiles downwards
   Arrow Left: Move tiles to the left
   Arrow Right: Move tiles to the right
   R: Reset the game

 # Game Interface

The game window will display the 2048 game grid. Each tile represents a number, and the goal is to combine tiles to reach the 2048 tile.

## The color scheme used in the game is as follows:

    Background color: (187, 173, 160)
    Tile colors:
        0: (205, 193, 180)
        2: (238, 228, 218)
        4: (237, 224, 200)
        8: (242, 177, 121)
        16: (245, 149, 99)
        32: (246, 124, 95)
        64: (246, 94, 59)
        128: (237, 207, 114)
        256: (237, 204, 97)
        512: (237, 200, 80)
        1024: (237, 197, 63)
        2048: (237, 194, 46)
    Text color: (119, 110, 101)
    Grid color: (187, 173, 160)
    Border color: (205, 193, 180)

# License

This project is licensed under the MIT License. Feel free to modify and distribute it as you like.

# Acknowledgments

This game was inspired by the original 2048 game created by Gabriele Cirulli. The Pygame library was used for graphics and event handling.
