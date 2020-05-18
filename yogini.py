import math
import pygame


"""
The Yogini: has a body and can perform Asanas
"""


class Yogini:

    def __init__(self):
        # set up the body from its parts
        self.body = Torso()

    def draw(self, screen):
        # draw each body part
        self.body.draw(screen)


class Bodypart:

    def __init__(self):
        self.thickness = 6
        self.color = (0, 0, 0)
        self.pos = (350, 200)  # spatial coordinates
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

    def draw(self, screen):
        # draw torso
        endpos = (self.x + self.length*math.sin(self.angle),
                  self.y - self.length*math.cos(self.angle))
        pygame.draw.line(screen, self.color, self.pos,
                         self.head.pos, self.thickness)
        # draw head
        self.head.pos = endpos
        self.head.angle = self.angle
        self.head.draw(screen)
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
        self.radius = 16
        self.neck_angle = 0
        super().__init__()
        self.color = (255, 0, 0)

    def draw(self, screen):
        angle = self.angle+self.neck_angle
        center_pos = (self.x+self.radius*math.sin(angle),
                      self.y-self.radius*math.cos(angle))
        rect = [center_pos[0]-self.radius, center_pos[1]-self.radius,
                self.radius*2, self.radius*2]
        pygame.draw.ellipse(screen, self.color, rect, 0)


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
        pygame.draw.line(screen, self.color, self.pos,
                         knee_pos, self.thickness)
        # draw lower leg
        angle += self.knee_angle
        foot_pos = (knee_pos[0]+self.length/2*math.sin(angle),
                    knee_pos[1]+self.length/2*math.cos(angle))
        pygame.draw.line(screen, self.color, knee_pos,
                         foot_pos, self.thickness)
        # draw foot
        angle += self.foot_angle
        if self.level_foot:
            angle = math.pi / 2
        toe_pos = (foot_pos[0]+self.length/6*math.sin(angle),
                   foot_pos[1]+self.length/6*math.cos(angle))
        pygame.draw.line(screen, self.color, foot_pos,
                         toe_pos, self.thickness)


class Arm(Bodypart):

    def __init__(self):
        self.length = 60
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
        pygame.draw.line(screen, self.color, self.pos,
                         elbow_pos, self.thickness)
        # draw lower arm
        angle += self.elbow_angle
        hand_pos = (elbow_pos[0]+self.length/2*math.sin(angle),
                    elbow_pos[1]+self.length/2*math.cos(angle))
        pygame.draw.line(screen, self.color, elbow_pos,
                         hand_pos, self.thickness)
        # draw hand
        angle += self.hand_angle
        if self.level_hand:
            angle = math.pi / 2
        finger_pos = (hand_pos[0]+self.length/8*math.sin(angle),
                      hand_pos[1]+self.length/8*math.cos(angle))
        pygame.draw.line(screen, self.color, hand_pos,
                         finger_pos, self.thickness)
