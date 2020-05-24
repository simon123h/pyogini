from gui import draw_line, Background
import pygame

class Studio:

    def __init__(self):
        # height of the ground
        self.ground_level = 640
        # background image
        self.background = Background('res/studio/studio.png', [0, 0])

    def draw(self, screen):
        # draw background image
        screen.blit(self.background.image, self.background.rect)
        # draw mat
        matpadding = 500
        size = pygame.display.get_surface().get_size()
        draw_line(screen, (40, 40, 80), (matpadding, self.ground_level),
                  (size[0]-matpadding, self.ground_level), 4)