import math
import numpy as np
from body import Body
from studio import Studio
from sequences import Sequence
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
        # our first sequence
        self.sequence = None
        # Start with a basic asana
        self.do_asana(Asana())

    def draw(self, screen):
        # draw the studio
        self.studio.draw(screen)
        # update the position of the body parts
        self.body.update()
        # draw each body part
        self.body.draw(screen)

    def live(self, time):
        # do everything a yogi does!
        asana, time_left = self.sequence.get_asana(time)
        transition_time = 0.75
        if time_left < transition_time:
            next_asana, _ = self.sequence.get_asana(time+transition_time)
            ratio = 1 - time_left / transition_time
            self.interpolate_asanas(asana, next_asana, ratio)
        else:
            self.do_asana(asana)

    def do_asana(self, asana):
        # general body rotation
        asana.orientate()
        self.body.angle = asana.angle
        # adapt all joint angles
        for my_joint, asana_joint in zip(self.body.joints, asana.joints):
            my_joint.angle = asana_joint.angle
        # update the position of all body parts
        self.body.update()
        # make sure that we always stand on the ground
        self.to_ground_level()

    def interpolate_asanas(self, asana1, asana2, ratio):
        # general body rotation
        asana1.orientate()
        asana2.orientate()
        self.body.angle = asana1.angle*(1-ratio) + asana2.angle*ratio
        # adapt all joint angles
        for my_joint, asana1_joint, asana2_joint in zip(self.body.joints, asana1.joints, asana2.joints):
            my_joint.angle = asana1_joint.angle*(1-ratio) + asana2_joint.angle*ratio
        # update the position of all body parts
        self.body.update()
        # make sure that we always stand on the ground
        self.to_ground_level()

    # make sure that we always stand on the ground
    def to_ground_level(self):
        miny = np.max([joint.y for joint in self.body.joints])
        self.body.pos = (self.body.pos[0],
                         self.body.pos[1]-miny+self.studio.ground_level-self.body.leg_l.thickness)
        self.body.update()

