#!/usr/bin/python3

import pygame
from yogini import Yogini


successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(
    successes, failures))

# screen = pygame.display.set_mode((1024, 720))
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
clock = pygame.time.Clock()
FPS = 60

# create the yogini
yogini = Yogini()

running = True
while running:
    # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    dt = clock.tick(FPS) / 1000
    screen.fill((255, 255, 255))  # Fill the screen with background color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            yogini.body.pos = [event.w / 2, event.h / 2]
        # elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_w:
        # elif event.type == pygame.KEYUP:

    yogini.draw(screen)

    pygame.display.update()  # Or pygame.display.flip()

print("Exited the game loop. Game will quit...")
