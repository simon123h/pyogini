import math
import numpy as np
import pygame
import pygame.gfxdraw
from asanas import Asana

"""
The Yogini: has a body and can perform Asanas
"""


class Yogini:

    def __init__(self):
        # The torso is the "head node" of the body
        self.body = Torso()
        # Start with a basic asana
        self.do_asana(Asana())
        # root body position
        ssize = pygame.display.get_surface().get_size()
        self.pos = [ssize[0] / 2, ssize[1] / 2]
        # body rotation
        self.angle = 0

    def draw(self, screen):
        # update the position of the body parts
        self.body.update()
        # draw each body part
        self.body.draw(screen)

    def do_asana(self, asana):
        # torso
        self.body.angle = asana.body_angle * math.pi/180
        # head
        self.body.head.neck_angle = asana.neck_angle * math.pi/180
        # arms
        self.body.arm_l.arm_angle = asana.arm_angle_l * math.pi/180
        self.body.arm_r.arm_angle = asana.arm_angle_r * math.pi / 180
        self.body.arm_l.elbow_angle = asana.elbow_angle_l * math.pi/180
        self.body.arm_r.elbow_angle = asana.elbow_angle_r * math.pi / 180
        self.body.arm_l.hand_angle = asana.hand_angle_l * math.pi/180
        self.body.arm_r.hand_angle = asana.hand_angle_r * math.pi / 180
        self.body.arm_l.level_hand = asana.level_hand_l
        self.body.arm_r.level_hand = asana.level_hand_r
        # legs
        self.body.leg_l.leg_angle = asana.leg_angle_l * math.pi/180
        self.body.leg_r.leg_angle = asana.leg_angle_r * math.pi / 180
        self.body.leg_l.knee_angle = asana.knee_angle_l * math.pi/180
        self.body.leg_r.knee_angle = asana.knee_angle_r * math.pi / 180
        self.body.leg_l.foot_angle = asana.foot_angle_l * math.pi/180
        self.body.leg_r.foot_angle = asana.foot_angle_r * math.pi / 180
        self.body.leg_l.level_foot = asana.level_foot_l
        self.body.leg_r.level_foot = asana.level_foot_r


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
        self.arm_l = Arm()
        self.arm_r = Arm()
        self.leg_l = Leg()
        self.leg_r = Leg()
        self.length = 70
        super().__init__()
        ssize = pygame.display.get_surface().get_size()
        self.pos = [ssize[0] / 2, ssize[1] / 2]

    # update the position and rotation of the joints
    def update(self):
        # update head position
        self.head.pos = (self.x + self.length*math.sin(self.angle),
                         self.y - self.length*math.cos(self.angle))
        self.head.angle = self.angle
        self.head.update()
        # update arm positions
        shoulderpos = (self.x + self.length*0.9*math.sin(self.angle),
                       self.y - self.length*0.9*math.cos(self.angle))
        self.arm_l.pos = shoulderpos
        self.arm_l.angle = self.angle
        self.arm_l.update()
        self.arm_r.pos = shoulderpos
        self.arm_r.angle = self.angle
        self.arm_r.update()
        # update leg positions
        self.leg_l.pos = self.pos
        self.leg_l.angle = self.angle
        self.leg_l.update()
        self.leg_r.pos = self.pos
        self.leg_r.angle = self.angle
        self.leg_r.update()

    def draw(self, screen):
        # draw head
        self.head.draw(screen)
        # draw torso
        draw_line(screen, self.color, self.pos, self.head.pos, self.thickness)
        # draw arms
        self.arm_l.draw(screen)
        self.arm_r.draw(screen)
        # draw legs
        self.leg_l.draw(screen)
        self.leg_r.draw(screen)


class Head(Bodypart):

    def __init__(self):
        self.radius = 18
        self.neck_angle = 0
        super().__init__()
        # self.color = (255, 0, 0)
        self.crown_pos = (0, 0)  # position of the crown

    def update(self):
        angle = self.angle+self.neck_angle
        self.crown_pos = (self.x+self.radius*math.sin(angle),
                          self.y-self.radius*math.cos(angle))

    def draw(self, screen):
        pygame.gfxdraw.filled_circle(screen, int(self.crown_pos[0]), int(
            self.crown_pos[1]), int(self.radius), self.color)
        pygame.gfxdraw.aacircle(screen, int(self.crown_pos[0]), int(
            self.crown_pos[1]), int(self.radius), self.color)
        pygame.gfxdraw.filled_circle(screen, int(self.crown_pos[0]), int(
            self.crown_pos[1]), int(self.radius*0.7), (255, 255, 255))
        pygame.gfxdraw.aacircle(screen, int(self.crown_pos[0]), int(
            self.crown_pos[1]), int(self.radius*0.7), (255, 255, 255))


class Arm(Bodypart):

    def __init__(self):
        self.length = 65
        self.arm_angle = 0
        self.elbow_angle = 0
        self.hand_angle = 0
        self.level_hand = False
        super().__init__()
        # self.color = (0, 255, 0)
        self.elbow_pos = (0, 0)
        self.hand_pos = (0, 0)
        self.finger_pos = (0, 0)

    def update(self):
        angle = -self.angle + self.arm_angle
        self.elbow_pos = (self.x+self.length/2*math.sin(angle),
                          self.y+self.length/2*math.cos(angle))
        angle += self.elbow_angle
        self.hand_pos = (self.elbow_pos[0]+self.length/2*math.sin(angle),
                         self.elbow_pos[1]+self.length/2*math.cos(angle))
        angle += -self.hand_angle
        if self.level_hand:
            angle = math.pi / 2
        self.finger_pos = (self.hand_pos[0]+self.length/10*math.sin(angle),
                           self.hand_pos[1]+self.length/10*math.cos(angle))

    def draw(self, screen):
        # draw upper arm
        draw_line(screen, self.color, self.pos,
                  self.elbow_pos, self.thickness)
        # draw lower arm
        draw_line(screen, self.color, self.elbow_pos,
                  self.hand_pos, self.thickness)
        # draw hand
        draw_line(screen, self.color, self.hand_pos,
                  self.finger_pos, self.thickness)


class Leg(Bodypart):

    def __init__(self):
        self.length = 100
        self.leg_angle = 0
        self.knee_angle = 0
        self.foot_angle = math.pi / 2
        self.level_foot = True
        super().__init__()
        # self.color = (0, 0, 255)
        self.knee_pos = (0, 0)
        self.foot_pos = (0, 0)
        self.toe_pos = (0, 0)

    def update(self):
        angle = -self.angle + self.leg_angle
        self.knee_pos = (self.x+self.length/2*math.sin(angle),
                         self.y+self.length/2*math.cos(angle))
        angle -= self.knee_angle
        self.foot_pos = (self.knee_pos[0]+self.length/2*math.sin(angle),
                         self.knee_pos[1]+self.length/2*math.cos(angle))
        angle += self.foot_angle
        if self.level_foot:
            angle = math.pi / 2
        self.toe_pos = (self.foot_pos[0]+self.length/6*math.sin(angle),
                        self.foot_pos[1]+self.length/6*math.cos(angle))

    def draw(self, screen):
        # draw upper leg
        draw_line(screen, self.color, self.pos,
                  self.knee_pos, self.thickness)
        # draw lower leg
        draw_line(screen, self.color, self.knee_pos,
                  self.foot_pos, self.thickness)
        # draw foot
        draw_line(screen, self.color, self.foot_pos,
                  self.toe_pos, self.thickness)


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
