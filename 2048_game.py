import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
width, height = 500, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048 Game")

# Set colors
background_color = (187, 173, 160)
tile_colors = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
text_color = (119, 110, 101)
grid_color = (187, 173, 160)
border_color = (205, 193, 180)

# Set the font
font = pygame.font.Font("arial.ttf", 48)

# Set the game grid dimensions
grid_size = 4
tile_size = 100
grid_padding = 20

# Calculate the positions of each tile
grid_start_x = (width - grid_size * tile_size - (grid_size - 1) * grid_padding) // 2
grid_start_y = (height - grid_size * tile_size - (grid_size - 1) * grid_padding) // 2

# Initialize the game grid
grid = [[0] * grid_size for _ in range(grid_size)]

# Function to add a new random tile (2 or 4) to the grid
def add_new_tile():
    empty_cells = [(i, j) for i in range(grid_size) for j in range(grid_size) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

# Function to draw the game grid
def draw_grid():
    pygame.draw.rect(window, background_color, (grid_start_x, grid_start_y, grid_size * tile_size + (grid_size - 1) * grid_padding, grid_size * tile_size + (grid_size - 1) * grid_padding))
    for i in range(grid_size):
        for j in range(grid_size):
            tile_value = grid[i][j]
            tile_color = tile_colors.get(tile_value, tile_colors[0])
            tile_x = grid_start_x + j * (tile_size + grid_padding)
            tile_y = grid_start_y + i * (tile_size + grid_padding)
            pygame.draw.rect(window, tile_color, (tile_x, tile_y, tile_size, tile_size))
            if tile_value != 0:
                text = font.render(str(tile_value), True, text_color)
                text_rect = text.get_rect()
                text_rect.center = (tile_x + tile_size // 2, tile_y + tile_size // 2)
                window.blit(text, text_rect)
            pygame.draw.rect(window, border_color, (tile_x, tile_y, tile_size, tile_size), 5)

# Function to handle tile movements
def move_tiles(direction):
    moved = False
    if direction == "up":
        for j in range(grid_size):
            for i in range(1, grid_size):
                if grid[i][j] != 0:
                    k = i - 1
                    while k >= 0 and grid[k][j] == 0:
                        grid[k][j] = grid[k + 1][j]
                        grid[k + 1][j] = 0
                        k -= 1
                        moved = True
                    if k >= 0 and grid[k][j] == grid[k + 1][j]:
                        grid[k][j] *= 2
                        grid[k + 1][j] = 0
                        moved = True
    elif direction == "down":
        for j in range(grid_size):
            for i in range(grid_size - 2, -1, -1):
                if grid[i][j] != 0:
                    k = i + 1
                    while k < grid_size and grid[k][j] == 0:
                        grid[k][j] = grid[k - 1][j]
                        grid[k - 1][j] = 0
                        k += 1
                        moved = True
                    if k < grid_size and grid[k][j] == grid[k - 1][j]:
                        grid[k][j] *= 2
                        grid[k - 1][j] = 0
                        moved = True
    elif direction == "left":
        for i in range(grid_size):
            for j in range(1, grid_size):
                if grid[i][j] != 0:
                    k = j - 1
                    while k >= 0 and grid[i][k] == 0:
                        grid[i][k] = grid[i][k + 1]
                        grid[i][k + 1] = 0
                        k -= 1
                        moved = True
                    if k >= 0 and grid[i][k] == grid[i][k + 1]:
                        grid[i][k] *= 2
                        grid[i][k + 1] = 0
                        moved = True
    elif direction == "right":
        for i in range(grid_size):
            for j in range(grid_size - 2, -1, -1):
                if grid[i][j] != 0:
                    k = j + 1
                    while k < grid_size and grid[i][k] == 0:
                        grid[i][k] = grid[i][k - 1]
                        grid[i][k - 1] = 0
                        k += 1
                        moved = True
                    if k < grid_size and grid[i][k] == grid[i][k - 1]:
                        grid[i][k] *= 2
                        grid[i][k - 1] = 0
                        moved = True
    return moved

# Function to handle game over
def game_over():
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                return False
            if i < grid_size - 1 and grid[i][j] == grid[i + 1][j]:
                return False
            if j < grid_size - 1 and grid[i][j] == grid[i][j + 1]:
                return False
    return True

# Initialize the game
add_new_tile()
add_new_tile()

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over():
                if event.key == pygame.K_UP:
                    moved = move_tiles("up")
                elif event.key == pygame.K_DOWN:
                    moved = move_tiles("down")
                elif event.key == pygame.K_LEFT:
                    moved = move_tiles("left")
                elif event.key == pygame.K_RIGHT:
                    moved = move_tiles("right")
                if moved:
                    add_new_tile()
            if event.key == pygame.K_r:
                # Reset the game
                grid = [[0] * grid_size for _ in range(grid_size)]
                add_new_tile()
                add_new_tile()

    # Clear the screen
    window.fill(background_color)

    # Draw the game grid
    draw_grid()

    # Check for game over
    if game_over():
        text = font.render("Game Over!", True, text_color)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        window.blit(text, text_rect)

    # Refresh the game screen
    pygame.display.flip()

# Quit the game
pygame.quit()
