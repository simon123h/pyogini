import math
import numpy as np
import pygame
import pygame.gfxdraw


"""
The Yogini: has a body and can perform Asanas
"""


class Yogini:

    def __init__(self):
        # The torso is the "head node" of the body
        self.body = Torso()

    def draw(self, screen):
        # draw each body part
        self.body.draw(screen)


class Bodypart:

    def __init__(self):
        self.thickness = 6
        self.color = (0, 0, 0)
        self.pos = (0, 0)  # spatial coordinates
        self.angle = 0  # rotation

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]


class Torso(Bodypart):

    def __init__(self):
        self.head = Head()
        self.arm_left = Arm()
        self.arm_right = Arm()
        self.leg_left = Leg()
        self.leg_right = Leg()
        self.length = 80
        super().__init__()
        ssize = pygame.display.get_surface().get_size()
        self.pos = [ssize[0] / 2, ssize[1] / 2]

    def draw(self, screen):
        # draw head
        neck_pos = (self.x + self.length*math.sin(self.angle),
            self.y - self.length*math.cos(self.angle))
        self.head.pos = neck_pos
        self.head.angle = self.angle
        self.head.draw(screen)
        # draw torso
        draw_line(screen, self.color, self.pos,
                  self.head.pos, self.thickness)
        # draw arms
        shoulderpos = (self.x + self.length*0.9*math.sin(self.angle),
                       self.y - self.length*0.9*math.cos(self.angle))
        self.arm_left.pos = shoulderpos
        self.arm_left.angle = self.angle
        self.arm_left.draw(screen)
        self.arm_right.pos = shoulderpos
        self.arm_right.angle = self.angle
        self.arm_right.draw(screen)
        # draw legs
        self.leg_left.pos = self.pos
        self.leg_left.angle = self.angle
        self.leg_left.draw(screen)
        self.leg_right.pos = self.pos
        self.leg_right.angle = self.angle
        self.leg_right.draw(screen)


class Head(Bodypart):

    def __init__(self):
        self.radius = 17
        self.neck_angle = 0
        super().__init__()
        self.color = (255, 0, 0)

    def draw(self, screen):
        angle = self.angle+self.neck_angle
        cpos = (self.x+self.radius*math.sin(angle),
                self.y-self.radius*math.cos(angle))
        pygame.gfxdraw.filled_circle(screen, int(cpos[0]), int(cpos[1]),
                                     int(self.radius), self.color)
        pygame.gfxdraw.aacircle(screen, int(cpos[0]), int(cpos[1]),
                                int(self.radius), self.color)
        pygame.gfxdraw.filled_circle(screen, int(cpos[0]), int(cpos[1]),
                                     int(self.radius*0.75), (255, 255, 255))
        pygame.gfxdraw.aacircle(screen, int(cpos[0]), int(cpos[1]),
                                int(self.radius*0.75), (255, 255, 255))


class Leg(Bodypart):

    def __init__(self):
        self.length = 96
        self.hip_angle = math.pi / 8
        self.knee_angle = -math.pi / 4
        self.foot_angle = math.pi / 2
        self.level_foot = True
        super().__init__()
        self.color = (0, 0, 255)

    def draw(self, screen):
        # draw upper leg
        angle = self.angle + self.hip_angle
        knee_pos = (self.x+self.length/2*math.sin(angle),
                    self.y+self.length/2*math.cos(angle))
        draw_line(screen, self.color, self.pos,
                  knee_pos, self.thickness)
        # draw lower leg
        angle += self.knee_angle
        foot_pos = (knee_pos[0]+self.length/2*math.sin(angle),
                    knee_pos[1]+self.length/2*math.cos(angle))
        draw_line(screen, self.color, knee_pos,
                  foot_pos, self.thickness)
        # draw foot
        angle += self.foot_angle
        if self.level_foot:
            angle = math.pi / 2
        toe_pos = (foot_pos[0]+self.length/6*math.sin(angle),
                   foot_pos[1]+self.length/6*math.cos(angle))
        draw_line(screen, self.color, foot_pos,
                  toe_pos, self.thickness)


class Arm(Bodypart):

    def __init__(self):
        self.length = 70
        self.arm_angle = 45*math.pi/180
        self.elbow_angle = 45*math.pi/180
        self.hand_angle = 90*math.pi/180
        self.level_hand = False
        super().__init__()
        self.color = (0, 255, 0)

    def draw(self, screen):
        # draw upper arm
        angle = self.angle + self.arm_angle
        elbow_pos = (self.x+self.length/2*math.sin(angle),
                     self.y+self.length/2*math.cos(angle))
        draw_line(screen, self.color, self.pos,
                  elbow_pos, self.thickness)
        # draw lower arm
        angle += self.elbow_angle
        hand_pos = (elbow_pos[0]+self.length/2*math.sin(angle),
                    elbow_pos[1]+self.length/2*math.cos(angle))
        draw_line(screen, self.color, elbow_pos,
                  hand_pos, self.thickness)
        # draw hand
        angle += self.hand_angle
        if self.level_hand:
            angle = math.pi / 2
        finger_pos = (hand_pos[0]+self.length/8*math.sin(angle),
                      hand_pos[1]+self.length/8*math.cos(angle))
        draw_line(screen, self.color, hand_pos,
                  finger_pos, self.thickness)


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
