import math
import numpy as np
from body import Body
from studio import Studio
from sequences import Sequence
from asanas import Asana
import pygame
import random

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
        self.asana = Asana()
        self.do_asana(self.asana)
        self.time_left = -1
        # was last breath in or out?
        self.last_breath = None
        # time [sec] for transitions between asanas
        self.transition_time = 1.5
        # font for position display
        self.font = pygame.font.SysFont('Comic Sans MS', 40)
        self.font_xs = pygame.font.SysFont('Comic Sans MS', 25)

    def draw(self, screen):
        # draw the studio
        self.studio.draw(screen)
        # update the position of the body parts
        self.body.update()
        # draw each body part
        self.body.draw(screen)
        # draw the name of the asana and the time left
        size = pygame.display.get_surface().get_size()
        textsurface = self.font.render(self.asana.name, False, (60, 60, 60))
        screen.blit(textsurface, (size[0]/2 -
                                  textsurface.get_rect().width/2, 40))
        textsurface = self.font_xs.render(self.asana.sanskrit, False, (60, 60, 60))
        screen.blit(textsurface, (size[0]/2 -
                                  textsurface.get_rect().width/2, 75))
        # io = "in" if self.last_breath == "i" else "out"
        # textsurface = self.font.render(str(len(self.asana.breath))+" breaths "+io, False, (50, 50, 50))
        # screen.blit(textsurface, (2*size[0]/3 -
        #                           textsurface.get_rect().width/2, 55))

    def live(self, time):
        # do everything a yogi does!
        # get the current asana of the sequence
        asana, time_left = self.sequence.get_asana(time)
        self.asana = asana
        self.time_left = time_left
        # do fancy transitions and perform the asanas
        time_in = asana.time - time_left
        transition_time = min(asana.time*0.8, self.transition_time)
        if time_in < transition_time:
            prev_asana, _ = self.sequence.get_asana(time, -1)
            ratio = time_in / transition_time
            ratio = 0.5*(1.1048*np.tanh(3*(ratio-0.5))+1)
            self.interpolate_asanas(prev_asana, asana, ratio)
        else:
            self.do_asana(asana)
        # breathe
        if asana.breath != "":
            breath_index = math.floor(time_in / asana.time * len(asana.breath))
            if breath_index < len(asana.breath):
                self.breathe(asana.breath[breath_index])

    # make breathing sounds
    def breathe(self, io):
        # don't breathe in twice...
        if io == self.last_breath:
            return
        random_id = str(random.randint(1, 3))
        # breathe in
        if io == "i":
            pygame.mixer.Sound("res/breath_in_"+random_id+".ogg").play()
            self.last_breath = io
        # breathe out
        if io == "o":
            pygame.mixer.Sound("res/breath_out_"+random_id+".ogg").play()
            self.last_breath = io

    def do_asana(self, asana):
        # general body rotation
        asana.orientate()
        self.body.angle = asana.angle
        self.body.bending = asana.bending
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
        self.body.bending = asana1.bending*(1-ratio) + asana2.bending*ratio
        # adapt all joint angles
        for my_joint, asana1_joint, asana2_joint in zip(
                self.body.joints, asana1.joints, asana2.joints):
            my_joint.angle = asana1_joint.angle * \
                (1-ratio) + asana2_joint.angle*ratio
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
