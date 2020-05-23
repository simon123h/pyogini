from gui import draw_line
import pygame

class Studio:

    def __init__(self):
        # height of the ground
        self.ground_level = 500

    def draw(self, screen):
        # draw bottom line
        size = pygame.display.get_surface().get_size()
        draw_line(screen, (40, 40, 80), (0, self.ground_level),
                  (size[0], self.ground_level), 4)