import math
from body import Body
from asanas import Asana

"""
The Yogini: has a body and can perform Asanas
"""


class Yogini:

    def __init__(self):
        # The torso is the "head node" of the body
        self.body = Body()
        # Start with a basic asana
        self.do_asana(Asana())

    def draw(self, screen):
        # update the position of the body parts
        self.body.update()
        # draw each body part
        self.body.draw(screen)

    def do_asana(self, asana):
        # torso
        self.body.angle = asana.angle * math.pi/180
        # head
        self.body.neck.angle = asana.neck.angle * math.pi/180
        # arms
        self.body.arm_l.shoulder.angle = asana.arm_l.shoulder.angle * math.pi/180
        self.body.arm_r.shoulder.angle = asana.arm_r.shoulder.angle * math.pi / 180
        self.body.arm_l.elbow.angle = asana.arm_l.elbow.angle * math.pi/180
        self.body.arm_r.elbow.angle = asana.arm_r.elbow.angle * math.pi / 180
        self.body.arm_l.hand.angle = asana.arm_l.hand.angle * math.pi/180
        self.body.arm_r.hand.angle = asana.arm_r.hand.angle * math.pi / 180
        self.body.arm_l.level_hand = asana.arm_l.level_hand
        self.body.arm_r.level_hand = asana.arm_r.level_hand
        # legs
        self.body.leg_l.hip.angle = asana.leg_l.hip.angle * math.pi/180
        self.body.leg_r.hip.angle = asana.leg_r.hip.angle * math.pi / 180
        self.body.leg_l.knee.angle = asana.leg_l.knee.angle * math.pi/180
        self.body.leg_r.knee.angle = asana.leg_r.knee.angle * math.pi / 180
        self.body.leg_l.foot.angle = asana.leg_l.foot.angle * math.pi/180
        self.body.leg_r.foot.angle = asana.leg_r.foot.angle * math.pi / 180
        self.body.leg_l.level_foot = asana.leg_l.level_foot
        self.body.leg_r.level_foot = asana.leg_r.level_foot
