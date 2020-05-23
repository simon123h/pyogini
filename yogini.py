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

    def draw(self, screen):
        # update the position of the body parts
        self.body.update()
        # draw each body part
        self.body.draw(screen)

    def do_asana(self, asana):
        # torso
        self.body.angle = asana.body_angle * math.pi/180
        # head
        self.body.head.neck.angle = asana.neck_angle * math.pi/180
        # arms
        self.body.arm_l.shoulder.angle = asana.shoulder_angle_l * math.pi/180
        self.body.arm_r.shoulder.angle = asana.shoulder_angle_r * math.pi / 180
        self.body.arm_l.elbow.angle = asana.elbow_angle_l * math.pi/180
        self.body.arm_r.elbow.angle = asana.elbow_angle_r * math.pi / 180
        self.body.arm_l.hand.angle = asana.hand_angle_l * math.pi/180
        self.body.arm_r.hand.angle = asana.hand_angle_r * math.pi / 180
        self.body.arm_l.level_hand = asana.level_hand_l
        self.body.arm_r.level_hand = asana.level_hand_r
        # legs
        self.body.leg_l.hip.angle = asana.hip_angle_l * math.pi/180
        self.body.leg_r.hip.angle = asana.hip_angle_r * math.pi / 180
        self.body.leg_l.knee.angle = asana.knee_angle_l * math.pi/180
        self.body.leg_r.knee.angle = asana.knee_angle_r * math.pi / 180
        self.body.leg_l.foot.angle = asana.foot_angle_l * math.pi/180
        self.body.leg_r.foot.angle = asana.foot_angle_r * math.pi / 180
        self.body.leg_l.level_foot = asana.level_foot_l
        self.body.leg_r.level_foot = asana.level_foot_r


class Joint:
    # A joint may be: the neck, the shoulders, ankles, knees, fingers, elbow... even fingers!

    def __init__(self):
        self.pos = (0, 0)
        self.angle = 0

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]


class Bodypart:

    def __init__(self):
        self.thickness = 6
        self.color = (0, 0, 0)
        self.angle = 0  # reference angle


class Torso(Bodypart):

    def __init__(self):
        self.length = 70
        self.head = Head()
        self.arm_l = Arm()
        self.arm_r = Arm()
        self.leg_l = Leg()
        self.leg_r = Leg()
        self.pos = (0, 0)  # spatial coordinates
        super().__init__()

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    # update the position and rotation of the joints
    def update(self):
        # update head position
        self.head.neck.pos = (self.x + self.length*math.sin(self.angle),
                              self.y - self.length*math.cos(self.angle))
        self.head.angle = self.angle
        self.head.update()
        # update arm positions
        self.arm_l.shoulder.pos = (self.x + self.length*0.9*math.sin(self.angle),
                                   self.y - self.length*0.9*math.cos(self.angle))
        self.arm_l.angle = self.angle
        self.arm_l.update()
        self.arm_r.shoulder.pos = self.arm_l.shoulder.pos
        self.arm_r.angle = self.angle
        self.arm_r.update()
        # update leg positions
        self.leg_l.hip.pos = self.pos
        self.leg_l.angle = self.angle
        self.leg_l.update()
        self.leg_r.hip.pos = self.leg_l.hip.pos
        self.leg_r.angle = self.angle
        self.leg_r.update()

    def level(self, joint_A, joint_B):
        pass

    def draw(self, screen):
        # draw head
        self.head.draw(screen)
        # draw torso
        draw_line(screen, self.color, self.pos,
                  self.head.neck.pos, self.thickness)
        # draw arms
        self.arm_l.draw(screen)
        self.arm_r.draw(screen)
        # draw legs
        self.leg_l.draw(screen)
        self.leg_r.draw(screen)


class Head(Bodypart):

    def __init__(self):
        self.radius = 18
        self.neck = Joint()  # the neck
        self.crown = Joint()  # position of the crown
        super().__init__()
        # self.color = (255, 0, 0)

    def update(self):
        angle = self.angle + self.neck.angle
        self.crown.pos = (self.neck.x+self.radius*math.sin(angle),
                          self.neck.y-self.radius*math.cos(angle))

    def draw(self, screen):
        pygame.gfxdraw.filled_circle(screen, int(self.crown.x), int(
            self.crown.y), int(self.radius), self.color)
        pygame.gfxdraw.aacircle(screen, int(self.crown.x), int(
            self.crown.y), int(self.radius), self.color)
        pygame.gfxdraw.filled_circle(screen, int(self.crown.x), int(
            self.crown.y), int(self.radius*0.7), (255, 255, 255))
        pygame.gfxdraw.aacircle(screen, int(self.crown.x), int(
            self.crown.y), int(self.radius*0.7), (255, 255, 255))


class Arm(Bodypart):

    def __init__(self):
        self.length = 65
        self.level_hand = False
        self.shoulder = Joint()
        self.elbow = Joint()
        self.hand = Joint()
        self.finger = Joint()
        super().__init__()
        # self.color = (0, 255, 0)

    def update(self):
        angle = -self.angle + self.shoulder.angle
        self.elbow.pos = (self.shoulder.x+self.length/2*math.sin(angle),
                          self.shoulder.y+self.length/2*math.cos(angle))
        angle += self.elbow.angle
        self.hand.pos = (self.elbow.x+self.length/2*math.sin(angle),
                         self.elbow.y+self.length/2*math.cos(angle))
        angle += -self.hand.angle
        if self.level_hand:
            angle = math.pi / 2
        self.finger.pos = (self.hand.x+self.length/10*math.sin(angle),
                           self.hand.y+self.length/10*math.cos(angle))

    def draw(self, screen):
        # draw upper arm
        draw_line(screen, self.color, self.shoulder.pos,
                  self.elbow.pos, self.thickness)
        # draw lower arm
        draw_line(screen, self.color, self.elbow.pos,
                  self.hand.pos, self.thickness)
        # draw hand
        draw_line(screen, self.color, self.hand.pos,
                  self.finger.pos, self.thickness)


class Leg(Bodypart):

    def __init__(self):
        self.length = 100
        self.level_foot = True
        self.hip = Joint()
        self.knee = Joint()
        self.foot = Joint()
        self.foot.angle = math.pi / 2
        self.toe = Joint()
        super().__init__()
        # self.color = (0, 0, 255)

    def update(self):
        angle = -self.angle + self.hip.angle
        self.knee.pos = (self.hip.x+self.length/2*math.sin(angle),
                         self.hip.y+self.length/2*math.cos(angle))
        angle -= self.knee.angle
        self.foot.pos = (self.knee.x+self.length/2*math.sin(angle),
                         self.knee.y+self.length/2*math.cos(angle))
        angle += self.foot.angle
        if self.level_foot:
            angle = math.pi / 2
        self.toe.pos = (self.foot.x+self.length/6*math.sin(angle),
                        self.foot.y+self.length/6*math.cos(angle))

    def draw(self, screen):
        # draw upper leg
        draw_line(screen, self.color, self.hip.pos,
                  self.knee.pos, self.thickness)
        # draw lower leg
        draw_line(screen, self.color, self.knee.pos,
                  self.foot.pos, self.thickness)
        # draw foot
        draw_line(screen, self.color, self.foot.pos,
                  self.toe.pos, self.thickness)


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
