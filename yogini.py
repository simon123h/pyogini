import math
import numpy as np
from body import Body
from studio import Studio
from asanas import Asana

"""
The Yogini: has a body and can perform Asanas
"""


class Yogini:

    def __init__(self):
        # We have a studio!
        self.studio = Studio()
        # The torso is the "head node" of the body
        self.body = Body()
        # Start with a basic asana
        self.do_asana(Asana())

    def draw(self, screen):
        # draw the studio
        self.studio.draw(screen)
        # update the position of the body parts
        self.body.update()
        # draw each body part
        self.body.draw(screen)

    def do_asana(self, asana):
        # general body rotation
        asana.orientate()
        self.body.angle = asana.angle
        # head
        self.body.neck.angle = asana.neck.angle
        # arms
        self.body.arm_l.shoulder.angle = asana.arm_l.shoulder.angle
        self.body.arm_r.shoulder.angle = asana.arm_r.shoulder.angle
        self.body.arm_l.elbow.angle = asana.arm_l.elbow.angle
        self.body.arm_r.elbow.angle = asana.arm_r.elbow.angle
        self.body.arm_l.hand.angle = asana.arm_l.hand.angle
        self.body.arm_r.hand.angle = asana.arm_r.hand.angle
        self.body.arm_l.level_hand = asana.arm_l.level_hand
        self.body.arm_r.level_hand = asana.arm_r.level_hand
        # legs
        self.body.leg_l.hip.angle = asana.leg_l.hip.angle
        self.body.leg_r.hip.angle = asana.leg_r.hip.angle
        self.body.leg_l.knee.angle = asana.leg_l.knee.angle
        self.body.leg_r.knee.angle = asana.leg_r.knee.angle
        self.body.leg_l.foot.angle = asana.leg_l.foot.angle
        self.body.leg_r.foot.angle = asana.leg_r.foot.angle
        self.body.leg_l.level_foot = asana.leg_l.level_foot
        self.body.leg_r.level_foot = asana.leg_r.level_foot
        # update the position of all body parts
        self.body.update()

        # make sure that we always stand on the ground
        self.body.update()
        joints = [self.body.neck, self.body.head.crown, self.body.arm_l.shoulder, self.body.arm_l.elbow, self.body.arm_l.hand, self.body.arm_l.finger, self.body.arm_r.shoulder, self.body.arm_r.elbow, self.body.arm_r.hand,
                  self.body.arm_r.finger, self.body.leg_l.hip, self.body.leg_l.knee, self.body.leg_l.foot, self.body.leg_l.toe, self.body.leg_r.hip, self.body.leg_r.knee, self.body.leg_r.foot, self.body.leg_r.toe]
        miny = np.max([joint.y for joint in joints])
        self.body.pos = (self.body.pos[0],
                         self.body.pos[1]-miny+self.studio.ground_level-self.body.leg_l.thickness)
        self.body.update()
