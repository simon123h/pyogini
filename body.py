import math
import pygame
import pygame.gfxdraw
from gui import draw_line


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


class Body(Bodypart):

    def __init__(self):
        self.length = 70
        self.head = Head()
        self.neck = self.head.neck
        self.arm_l = Arm()
        self.arm_r = Arm()
        self.leg_l = Leg()
        self.leg_r = Leg()
        self.pos = (0, 0)  # spatial coordinates
        # list of all joints
        self.joints = [self.neck, self.head.crown,
                       self.arm_l.shoulder, self.arm_l.elbow, self.arm_l.hand, self.arm_l.finger,
                       self.arm_r.shoulder, self.arm_r.elbow, self.arm_r.hand, self.arm_r.finger,
                       self.leg_l.hip, self.leg_l.knee, self.leg_l.foot, self.leg_l.toe,
                       self.leg_r.hip, self.leg_r.knee, self.leg_r.foot, self.leg_r.toe]
        super().__init__()

    # update the position and rotation of the joints
    def update(self):
        # update head position
        angle = self.angle * math.pi / 180
        self.head.neck.pos = (self.pos[0] + self.length*math.sin(angle),
                              self.pos[1] - self.length*math.cos(angle))
        self.head.angle = self.angle
        self.head.update()
        # update arm positions
        self.arm_l.shoulder.pos = (self.pos[0] + self.length*0.9*math.sin(angle),
                                   self.pos[1] - self.length*0.9*math.cos(angle))
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
        angle = (self.angle + self.neck.angle) * math.pi / 180
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
        angle = (-self.angle + self.shoulder.angle) * math.pi / 180
        self.elbow.pos = (self.shoulder.x+self.length/2*math.sin(angle),
                          self.shoulder.y+self.length/2*math.cos(angle))
        angle += self.elbow.angle * math.pi / 180
        self.hand.pos = (self.elbow.x+self.length/2*math.sin(angle),
                         self.elbow.y+self.length/2*math.cos(angle))
        angle += -self.hand.angle * math.pi / 180
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
        angle = (-self.angle + self.hip.angle) * math.pi / 180
        self.knee.pos = (self.hip.x+self.length/2*math.sin(angle),
                         self.hip.y+self.length/2*math.cos(angle))
        angle -= self.knee.angle * math.pi / 180
        self.foot.pos = (self.knee.x+self.length/2*math.sin(angle),
                         self.knee.y+self.length/2*math.cos(angle))
        angle += self.foot.angle * math.pi / 180
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
