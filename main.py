#!/usr/bin/python3

import pygame
from yogini import Yogini
import sequences

successes, failures = pygame.init()

screen = pygame.display.set_mode((1280, 720))
# screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
clock = pygame.time.Clock()
FPS = 60

# create the yogini
yogini = Yogini()
ssize = pygame.display.get_surface().get_size()
yogini.body.pos = [ssize[0] / 2, ssize[1] / 2]
yogini.sequence = sequences.ashtanga

time = 0

running = True
while running:
    # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    dt = clock.tick(FPS) / 1000
    time += dt
    screen.fill((255, 218, 148))  # Fill the screen with background color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            yogini.body.pos = [event.w / 2, event.h / 2]

    # let the yogini live
    yogini.live(time)

    # ...and draw it
    yogini.draw(screen)

    pygame.display.update()

print("Exited the game loop. Game will quit...")
