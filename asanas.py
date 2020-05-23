from body import Body
import math


class Asana(Body):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.sanskrit = ""
        # the breath pattern
        self.breath = "io"
        self.time = 5
        # head
        self.neck.angle = 0
        # arms
        self.arm_l.shoulder.angle = 45
        self.arm_r.shoulder.angle = 45
        self.arm_l.elbow.angle = 45
        self.arm_r.elbow.angle = 45
        self.arm_l.hand.angle = 90
        self.arm_r.hand.angle = 90
        # legs
        self.leg_l.hip.angle = 0
        self.leg_r.hip.angle = 0
        self.leg_l.knee.angle = 0
        self.leg_r.knee.angle = 0
        self.leg_l.foot.angle = 90
        self.leg_r.foot.angle = 90

    # make sure that we have the correct orientation (orientation fct. vanishes)
    def orientate(self):
        self.align_joints(self.leg_l.hip, self.leg_l.foot, 90)

    # align two given joints so that they build a given angle with the ground
    def align_joints(self, joint1, joint2, angle=0):
        self.update()
        self.angle += angle + self.angle_with_ground(joint1, joint2)

    def align_hands_with_ground(self, left=True, right=True):
        self.update()
        if left:
            self.arm_l.hand.angle = -self.angle_with_ground(self.arm_l.elbow, self.arm_l.hand)
        if right:
            self.arm_r.hand.angle = -self.angle_with_ground(self.arm_r.elbow, self.arm_r.hand)

    def align_feet_with_ground(self, left=True, right=True):
        self.update()
        if left:
            self.leg_l.foot.angle = -self.angle_with_ground(self.leg_l.knee, self.leg_l.foot)
        if right:
            self.leg_r.foot.angle = -self.angle_with_ground(self.leg_r.knee, self.leg_r.foot)

    # returns the angle between the line between two joints and thr ground
    @staticmethod
    def angle_with_ground(joint1, joint2):
        return math.atan2(joint1.y - joint2.y, joint2.x - joint1.x) * 180 / math.pi

    def sync_arms_lr(self):
        self.arm_r.shoulder.angle = self.arm_l.shoulder.angle
        self.arm_r.elbow.angle = self.arm_l.elbow.angle
        self.arm_r.hand.angle = self.arm_l.hand.angle

    def sync_arms_rl(self):
        self.arm_l.shoulder.angle = self.arm_r.shoulder.angle
        self.arm_l.elbow.angle = self.arm_r.elbow.angle
        self.arm_l.hand.angle = self.arm_r.hand.angle

    def sync_legs_lr(self):
        self.leg_r.hip.angle = self.leg_l.hip.angle
        self.leg_r.knee.angle = self.leg_l.knee.angle
        self.leg_r.foot.angle = self.leg_l.foot.angle

    def sync_legs_rl(self):
        self.leg_l.hip.angle = self.leg_r.hip.angle
        self.leg_l.knee.angle = self.leg_r.knee.angle
        self.leg_l.foot.angle = self.leg_r.foot.angle

    def sync_lr(self):
        self.sync_arms_lr()
        self.sync_legs_lr()

    def sync_rl(self):
        self.sync_arms_rl()
        self.sync_legs_rl()


class Standing(Asana):

    def __init__(self):
        super().__init__()
        self.name = "Mountain Pose"
        self.sanskrit = "Tadasana"
        # head
        self.head.neck.angle = 0
        # arms
        self.arm_l.shoulder.angle = 0
        self.arm_l.elbow.angle = 0
        self.arm_l.hand.angle = 0
        self.arm_l.shoulder.angle = 10
        self.arm_l.elbow.angle = 140
        self.arm_l.hand.angle = 0
        # legs
        self.leg_l.hip.angle = 0
        self.leg_l.knee.angle = 0
        self.leg_l.foot.angle = 90
        # sync left-right
        self.sync_lr()

    # let the hip be above the feet
    def orientate(self):
        self.align_joints(self.leg_l.hip, self.leg_l.foot, 90)


class UpwardSalute(Standing):
    def __init__(self):
        super().__init__()
        self.name = "Upward Salute"
        self.sanskrit = "Urdhva Hastasana"
        self.arm_l.shoulder.angle = 170
        self.arm_l.elbow.angle = 0
        self.arm_l.hand.angle = 0
        self.head.neck.angle = -20
        # sync left-right
        self.sync_lr()


class ForwardFold(Standing):
    def __init__(self):
        super().__init__()
        self.name = "Forward Fold"
        self.sanskrit = "Uttanasana"
        self.leg_l.hip.angle = 122
        self.arm_l.shoulder.angle = 100
        self.arm_l.elbow.angle = 0
        self.arm_l.hand.angle = 0
        self.head.neck.angle = 50
        # sync left-right
        self.sync_lr()


class HalfwayLift(ForwardFold):
    def __init__(self):
        super().__init__()
        self.name = "Halfway Fold"
        self.sanskrit = "Ardha Uttanasana"
        self.head.neck.angle = -20
        # sync left-right
        self.sync_lr()


class Plank(Asana):
    def __init__(self):
        super().__init__()
        self.arm_l.shoulder.angle = 80
        self.arm_l.elbow.angle = 0
        self.arm_l.hand.angle = 70
        self.leg_l.hip.angle = 5
        self.leg_l.foot.angle = 80
        self.sync_lr()

    # let the toes and hands touch the ground
    def orientate(self):
        self.align_hands_with_ground()
        self.align_joints(self.leg_l.toe, self.arm_l.hand, 0)


class LowLunge(Plank):
    def __init__(self):
        super().__init__()
        self.leg_r.hip.angle = 166.5
        self.leg_r.knee.angle = 90
        self.name = "Low Lunge"
        self.sanskrit = "Ashwa Sanchalanasana"

    # let the toes and hands touch the ground
    def orientate(self):
        self.align_hands_with_ground()
        self.align_feet_with_ground(left=False)
        self.align_joints(self.leg_l.toe, self.arm_l.hand, 0)


class Chaturanga(Plank):
    def __init__(self):
        super().__init__()
        self.name = "Ashtanga Chaturanga"
        self.sanskrit = "Ashtanga Chaturanga"
        self.angle = 90
        self.head.neck.angle = -20
        self.arm_l.shoulder.angle = -40
        self.arm_l.elbow.angle = 120
        self.leg_l.hip.angle = 0
        self.leg_l.foot.angle = 80
        self.sync_lr()


class UpDog(Chaturanga):
    def __init__(self):
        super().__init__()
        self.name = "Upward Facing Dog"
        self.angle = 60
        self.head.neck.angle = -40
        self.leg_l.hip.angle = -15
        self.leg_l.foot.angle = 0
        self.arm_l.shoulder.angle = 65
        self.arm_l.elbow.angle = 0
        self.sync_lr()


class DownDog(Asana):
    def __init__(self):
        super().__init__()
        self.name = "Downward Facing Dog"
        self.head.neck.angle = 20
        self.leg_l.hip.angle = 85
        self.arm_l.shoulder.angle = 190
        self.arm_l.elbow.angle = 0
        self.sync_lr()

    # let the toes and hands touch the ground
    def orientate(self):
        self.align_hands_with_ground()
        self.align_joints(self.leg_l.toe, self.arm_l.hand, 0)



class ChildsPose(Asana):
    def __init__(self):
        super().__init__()
        self.name = "Child's Pose"
        self.sanskrit = "Balasana"
        self.head.neck.angle = -20
        self.leg_l.hip.angle = 155
        self.leg_l.knee.angle = 150
        self.leg_l.foot.angle = 20
        self.arm_l.shoulder.angle = 170
        self.arm_l.elbow.angle = 0
        self.sync_lr()

    # let the toes and hands touch the ground
    def orientate(self):
        self.align_hands_with_ground()
        self.align_joints(self.leg_l.toe, self.arm_l.hand, 0)



class AllFours(Asana):
    def __init__(self):
        super().__init__()
        self.name = "On All Fours"
        self.head.neck.angle = 0
        self.leg_l.hip.angle = 80
        self.leg_l.knee.angle = 90
        self.leg_l.foot.angle = 10
        self.arm_l.shoulder.angle = 90
        self.arm_l.elbow.angle = 20
        self.sync_lr()

    # let the toes and hands touch the ground
    def orientate(self):
        self.align_hands_with_ground()
        self.align_joints(self.leg_l.toe, self.arm_l.hand, 0)


class Cat(AllFours):
    def __init__(self):
        super().__init__()
        self.name = "Cat"
        self.sanskrit = "Cakravakasana"
        self.head.neck.angle = 30
        self.bending = 30
        self.sync_lr()


class Cow(AllFours):
    def __init__(self):
        super().__init__()
        self.name = "Cow"
        self.sanskrit = "Bitilasana"
        self.head.neck.angle = -30
        self.bending = -30
        self.sync_lr()


class Chair(Standing):
    def __init__(self):
        super().__init__()
        self.name = "Chair Pose"
        self.sanskrit = "Utkatasana"
        self.bending = -30
        self.leg_l.hip.angle = 90
        self.leg_l.knee.angle = 100
        self.arm_l.shoulder.angle = 150
        self.arm_l.elbow.angle = 0
        self.arm_l.hand.angle = 0
        self.head.neck.angle = -20
        # sync left-right
        self.sync_lr()

    # let the hip be above the feet
    def orientate(self):
        self.align_feet_with_ground()
        self.align_joints(self.arm_l.shoulder, self.leg_l.toe, 90)


class Warrior1(Plank):
    def __init__(self):
        super().__init__()
        self.leg_l.hip.angle = 5-40
        self.leg_r.hip.angle = 166.5-40
        self.leg_r.knee.angle = 90
        self.bending = -30
        self.neck.angle = -20
        self.arm_l.shoulder.angle = 190
        self.arm_l.hand.angle = 0
        self.sync_arms_lr()

    # let the toes and hands touch the ground
    def orientate(self):
        self.align_feet_with_ground(left=False)
        self.align_joints(self.leg_l.toe, self.leg_r.foot, 0)