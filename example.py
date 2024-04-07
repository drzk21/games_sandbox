import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Maze settings
cols, rows = 20, 15
cell_size = width // cols

# Generate a simple maze (for simplicity, we'll use a random pattern)
maze = np.random.choice([0, 1], size=(rows, cols), p=[0.2, 0.8])

# Player settings
player_pos = [0, 0]  # Start in the top-left corner
player_color = green
goal_pos = [cols-1, rows-1]  # Goal is at the bottom-right corner
goal_color = red
score = cols * rows * 10  # Starting score

# Text
font = pygame.font.SysFont('arial', 24)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_pos[0] > 0:
                player_pos[0] -= 1
                score -= 1
            elif event.key == pygame.K_RIGHT and player_pos[0] < cols-1:
                player_pos[0] += 1
                score -= 1
            elif event.key == pygame.K_UP and player_pos[1] > 0:
                player_pos[1] -= 1
                score -= 1
            elif event.key == pygame.K_DOWN and player_pos[1] < rows-1:
                player_pos[1] += 1
                score -= 1

    # Display the score
    text = font.render(str(score), True, (255, 92, 255))
    textRect = text.get_rect()

    # Draw the maze
    screen.fill(black)
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, white if maze[y][x] == 1 else black, rect)

    # Draw the player and goal
    pygame.draw.rect(screen, player_color, (player_pos[0]*cell_size, player_pos[1]*cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, goal_color, (goal_pos[0]*cell_size, goal_pos[1]*cell_size, cell_size, cell_size))

    screen.blit(text, textRect)

    # Check for reaching the goal
    if player_pos == goal_pos:
        print(f"You reached the goal! Your score: {score}")
        running = False

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
