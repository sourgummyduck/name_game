# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from random import randint

pygame.init()

def create_background():
    # Set up the drawing window
    screen = pygame.display.set_mode([800, 800])
    # Fill the background with white
    screen.fill((255, 255, 255))

    return screen


def create_sprite():
    # Draw a solid blue circle in the center
    return Rect(100, 100, 50, 50)

def check_collision(player, speed_x, speed_y, direction):
    if player.left < 20 or player.right > 1260:
        direction += -1
        speed_x = randint(0, 5) * direction
        speed_y = randint(0, 5) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction

    if player.top < 20 or player.right > 780:
        direction += -1
        speed_x = randint(0, 5) * direction
        speed_y = randint(0, 5) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction

    player.left += speed_x
    player.top += speed_y

    return player

# --------------------------------------------------------------------------------

# Run until the user asks to quit
running = True
screen = create_background()

# Create clock
clock = pygame.time.Clock()

direction = 1
speed_x = 5
speed_y = 4

player = create_sprite()

# TODO: Create list for players
# TODO: Create check for collissions 
# TODO: Create check for corners
# TODO: Create mechanism for input 

while running:
    # Set FPS to 60
    clock.tick(60)
    
    # Collission for walls 
    if player.left <= 20 or player.right >= 780:
        direction *= -1
        speed_x = randint(0, 5) * direction
        speed_y = randint(0, 5) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 5) * direction
            speed_y = randint(2, 5) * direction

    if player.top <= 20 or player.bottom >= 780:
        direction *= -1
        speed_x = randint(0, 5) * direction
        speed_y = randint(0, 5) * direction

        if speed_x == 0 and speed_y == 0:
            speed_x = randint(0, 5) * direction
            speed_y = randint(0, 5) * direction

    player.left += speed_x
    player.top += speed_y

    pygame.draw.rect(screen, (0,   255,   0), player)
    pygame.display.update()
    screen.fill((255, 255, 255))

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Done! Time to quit.
pygame.quit()

