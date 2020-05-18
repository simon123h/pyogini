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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()  # Get rect of same size as 'image'.
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)


player = Player()
yogini = Yogini()
running = True
while running:
    # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    dt = clock.tick(FPS) / 1000
    screen.fill(WHITE)  # Fill the screen with background color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            # ssize = pygame.display.get_surface().get_size()
            yogini.body.pos = [event.w / 2, event.h / 2]
            print("resize:", yogini.body.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.velocity[1] = -200 * dt  # 200 pixels per second
            elif event.key == pygame.K_s:
                player.velocity[1] = 200 * dt
            elif event.key == pygame.K_a:
                player.velocity[0] = -200 * dt
            elif event.key == pygame.K_d:
                player.velocity[0] = 200 * dt
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.velocity[1] = 0
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                player.velocity[0] = 0

    player.update()
    screen.blit(player.image, player.rect)

    yogini.draw(screen)

    pygame.display.update()  # Or pygame.display.flip()

print("Exited the game loop. Game will quit...")
