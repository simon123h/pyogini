

class Asana:

    def __init__(self):
        self.name = ""
        self.sanskrit = ""
        # torso
        self.body_angle = 0
        # head
        self.neck_angle = 0
        # arms
        self.arm_angle_l = 45
        self.arm_angle_r = 45
        self.elbow_angle_l = 45
        self.elbow_angle_r = 45
        self.hand_angle_l = 90
        self.hand_angle_r = 90
        self.level_hand_l = False
        self.level_hand_r = False
        # legs
        self.leg_angle_l = 0
        self.leg_angle_r = 0
        self.knee_angle_l = 0
        self.knee_angle_r = 0
        self.foot_angle_l = 90
        self.foot_angle_r = 90
        self.level_foot_l = True
        self.level_foot_r = True

    def sync_arms_lr(self):
        self.arm_angle_r = self.arm_angle_l
        self.elbow_angle_r = self.elbow_angle_l
        self.hand_angle_r = self.hand_angle_l
        self.level_hand_r = self.level_hand_l

    def sync_arms_rl(self):
        self.arm_angle_l = self.arm_angle_r
        self.elbow_angle_l = self.elbow_angle_r
        self.hand_angle_l = self.hand_angle_r
        self.level_hand_l = self.level_hand_r

    def sync_legs_lr(self):
        self.leg_angle_r = self.leg_angle_l
        self.knee_angle_r = self.knee_angle_l
        self.foot_angle_r = self.foot_angle_l
        self.level_foot_r = self.level_foot_l

    def sync_legs_rl(self):
        self.leg_angle_l = self.leg_angle_r
        self.knee_angle_l = self.knee_angle_r
        self.foot_angle_l = self.foot_angle_r
        self.level_foot_l = self.level_foot_r

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
        # torso
        self.body_angle = 0
        # head
        self.neck_angle = 0
        # arms
        self.arm_angle_l = 0
        self.elbow_angle_l = 0
        self.hand_angle_l = 0
        self.level_hand_l = False
        self.arm_angle_l = 10
        self.elbow_angle_l = 140
        self.hand_angle_l = -20
        # legs
        self.leg_angle_l = 0
        self.knee_angle_l = 0
        self.foot_angle_l = 90
        self.level_foot_l = True
        # sync left-right
        self.sync_lr()


class UpwardSalute(Standing):
    def __init__(self):
        super().__init__()
        self.name = "Upward Salute"
        self.sanskrit = "Urdhva Hastasana"
        self.arm_angle_l = 170
        self.elbow_angle_l = 0
        self.hand_angle_l = 0
        self.neck_angle = -20
        # sync left-right
        self.sync_lr()


class ForwardFold(Standing):
    def __init__(self):
        super().__init__()
        self.name = "Forward Fold"
        self.sanskrit = "Uttanasana"
        self.body_angle = 122
        self.leg_angle_l = 122
        self.arm_angle_l = 100
        self.elbow_angle_l = 0
        self.hand_angle_l = 0
        self.neck_angle = 50
        # sync left-right
        self.sync_lr()


class HalfwayLift(ForwardFold):
    def __init__(self):
        super().__init__()
        self.sanskrit = "Ardha Uttanasana"
        self.neck_angle = -20
        # sync left-right
        self.sync_lr()


class Plank(Standing):
    def __init__(self):
        super().__init__()
        self.body_angle = 77
        self.arm_angle_l = 80
        self.elbow_angle_l = 0
        self.level_hand_l = True
        self.leg_angle_l = 5
        self.level_foot_l = False
        self.foot_angle_l = 80
        self.sync_lr()


class Chaturanga(Plank):
    def __init__(self):
        super().__init__()
        self.name = "Ashtanga Chaturanga"
        self.sanskrit = "Ashtanga Chaturanga"
        self.body_angle = 90
        self.neck_angle = -20
        self.arm_angle_l = -40
        self.elbow_angle_l = 120
        self.level_hand_l = True
        self.leg_angle_l = 0
        self.level_foot_l = False
        self.foot_angle_l = 80
        self.sync_lr()


class UpDog(Chaturanga):
    def __init__(self):
        super().__init__()
        self.name = "Upward Facing Dog"
        self.body_angle = 65
        self.neck_angle = -40
        self.leg_angle_l = -15
        self.level_foot_l = False
        self.foot_angle_l = 0
        self.arm_angle_l = 65
        self.elbow_angle_l = 0
        self.sync_lr()



class DownDog(Asana):
    def __init__(self):
        super().__init__()
        self.name = "Downward Facing Dog"
        self.name = "Upwards Facing Dog"
        self.body_angle = 130
        self.neck_angle = 20
        self.leg_angle_l = 85
        self.level_foot_l = True
        self.level_hand_l = True
        self.arm_angle_l = 190
        self.elbow_angle_l = 0
        self.sync_lr()


class Lunge(Plank):
    def __init__(self):
        super().__init__()
        self.leg_angle_r = 170
        self.knee_angle_r = 90
        self.level_foot_r = True
