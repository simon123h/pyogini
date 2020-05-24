
import math
import numpy as np
import pygame
import pygame.gfxdraw


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# draw an anti-aliased line with rounded corners
def draw_line(screen, color, X0, X1, thickness):
    X0 = np.array(X0)
    X1 = np.array(X1)
    center_L1 = (X0 + X1) / 2
    length = np.linalg.norm(X0-X1)
    angle = math.atan2(X0[1] - X1[1], X0[0] - X1[0])
    UL = (center_L1[0] + (length / 2.) * math.cos(angle) - (thickness / 2.) * math.sin(angle),
          center_L1[1] + (thickness / 2.) * math.cos(angle) + (length / 2.) * math.sin(angle))
    UR = (center_L1[0] - (length / 2.) * math.cos(angle) - (thickness / 2.) * math.sin(angle),
          center_L1[1] + (thickness / 2.) * math.cos(angle) - (length / 2.) * math.sin(angle))
    BL = (center_L1[0] + (length / 2.) * math.cos(angle) + (thickness / 2.) * math.sin(angle),
          center_L1[1] - (thickness / 2.) * math.cos(angle) + (length / 2.) * math.sin(angle))
    BR = (center_L1[0] - (length / 2.) * math.cos(angle) + (thickness / 2.) * math.sin(angle),
          center_L1[1] - (thickness / 2.) * math.cos(angle) - (length / 2.) * math.sin(angle))
    pygame.gfxdraw.aapolygon(screen, (UL, UR, BR, BL), color)
    pygame.gfxdraw.filled_polygon(screen, (UL, UR, BR, BL), color)
    pygame.gfxdraw.aacircle(screen, int(
        X0[0]), int(X0[1]), int(thickness/2), color)
    pygame.gfxdraw.filled_circle(screen, int(
        X0[0]), int(X0[1]), int(thickness/2), color)
    pygame.gfxdraw.aacircle(screen, int(
        X1[0]), int(X1[1]), int(thickness/2), color)
    pygame.gfxdraw.filled_circle(screen, int(
        X1[0]), int(X1[1]), int(thickness/2), color)


# draw a parabolic arc that consists of line segments
def draw_parabola(screen, color, X0, X1, bow, thickness, nsegments=20):
    X0 = np.array(X0)
    X1 = np.array(X1)
    dx = np.linalg.norm(X1-X0)/nsegments
    # unit vectors
    unit_x = (X1-X0)
    unit_x /= np.linalg.norm(unit_x)
    unit_y = np.array([-unit_x[1], unit_x[0]])
    X_old = X0
    for n in range(nsegments+1):
        X_new = X0 + n*unit_x*dx + bow * ((n/nsegments-0.5)**2 - 0.25) * unit_y
        draw_line(screen, color, X_old, X_new, thickness)
        X_old = X_new
