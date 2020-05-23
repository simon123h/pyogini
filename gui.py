
import numpy as np
import pygame
import pygame.gfxdraw


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
