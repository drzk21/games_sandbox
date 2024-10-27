# Imports
import pygame
import random
import math

# Initialize
pygame.init()

# Flags


# Constants
width = 500
height = 500
colors = ['violet', 'cyan', 'yellow', 'blue']

# Canvas
canvas = pygame.display.set_mode((width, height)) 

# Title
pygame.display.set_caption("Color Grid") 
exit = False

# Functions
def drawGrid(colors):
    sideLength = math.floor(width / 5)
    colorLength = len(colors)
    colorSelect = 0
    for x in range(0, width, sideLength):
        for y in range(0, height, sideLength):
            rect = pygame.Rect(x, y, sideLength, sideLength)
            pygame.draw.rect(canvas, colors[colorSelect % colorLength], rect, 10)
            colorSelect += 1


# Main program
while not exit: 
    drawGrid(colors)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 