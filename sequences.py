from asanas import *

SPEED=2

class Sequence:

    def __init__(self, name):
        self.name = name
        self.asanas = []
        self.breath_duration = 4/SPEED

    def add_asana(self, asana, breath=None, time=None):
        self.asanas.append(asana)
        if time is None:
            time = 2 if breath is None else self.breath_duration * len(breath)
        asana.time = time
        if breath is not None:
            asana.breath = breath

    def append_sequence(self, sequence):
        self.asanas += sequence.asanas

    def get_asana(self, time, shift_index=0):
        # time = time % self.total_time()
        if time >= self.total_time():
            return self.asanas[-1], self.total_time() - time
        index = -1
        while time >= 0:
            index += 1
            time -= self.asanas[index].time
        index += shift_index
        index = max(index, 0)
        return self.asanas[index], -time

    def total_time(self):
        return sum([a.time for a in self.asanas])



meditation = Sequence("Meditation")
meditation.add_asana(ChildsPose(), "oi"*15)

catcow = Sequence("Cat&Cow")
catcow.add_asana(AllFours(), "io"*2)
for i in range(5):
    catcow.add_asana(Cow(), "i")
    catcow.add_asana(Cat(), "o")


vinyasa_cat_to_stand = Sequence("Vinyasa")
vinyasa_cat_to_stand.add_asana(AllFours(), "i")
vinyasa_cat_to_stand.add_asana(DownDog(), "o")
vinyasa_cat_to_stand.add_asana(LegToChest(), time=1.5/SPEED, breath="")
vinyasa_cat_to_stand.add_asana(LowLunge(), "i")
vinyasa_cat_to_stand.add_asana(ForwardFold(), "o")
vinyasa_cat_to_stand.add_asana(UpwardSalute(), "i")
vinyasa_cat_to_stand.add_asana(Standing(), "o")

sun_A = Sequence("Sun Salutation A")
sun_A.add_asana(Standing(), "o")
sun_A.add_asana(UpwardSalute(), "i")
sun_A.add_asana(ForwardFold(), "o")
sun_A.add_asana(HalfwayLift(), "i")
sun_A.add_asana(LowLunge(), "o")
sun_A.add_asana(LegToChest(), time=1.5/SPEED, breath="")
sun_A.add_asana(Plank(), "i")
sun_A.add_asana(Chaturanga(), "o")
sun_A.add_asana(UpDog(), "i")
sun_A.add_asana(DownDog(), "oioio")
sun_A.add_asana(LegToChest(), time=1.5/SPEED, breath="")
sun_A.add_asana(LowLunge(), "i")
sun_A.add_asana(ForwardFold(), "o")
sun_A.add_asana(UpwardSalute(), "i")
sun_A.add_asana(Standing(), "o")

sun_B = Sequence("Sun Salutation B")
sun_B.add_asana(Chair(), "ioi")
sun_B.add_asana(ForwardFold(), "o")
sun_B.add_asana(HalfwayLift(), "i")
sun_B.add_asana(LowLunge(), "o")
sun_B.add_asana(LegToChest(), time=1.5/SPEED, breath="")
sun_B.add_asana(Plank(), "i")
sun_B.add_asana(Chaturanga(), "o")
sun_B.add_asana(UpDog(), "i")
sun_B.add_asana(DownDog(), "o")
sun_B.add_asana(LegToChest(), time=1/SPEED, breath="")
sun_B.add_asana(LowLunge(), time=1/SPEED, breath="")
sun_B.add_asana(Warrior1(), "i")
sun_B.add_asana(LowLunge(), "o")
sun_B.add_asana(LegToChest(), time=1.5/SPEED, breath="")
sun_B.add_asana(Plank(), "i")
sun_B.add_asana(Chaturanga(), "o")
sun_B.add_asana(UpDog(), "i")
sun_B.add_asana(DownDog(), "o")
sun_B.add_asana(LegToChest(), time=1/SPEED, breath="")
sun_B.add_asana(LowLunge(), time=1/SPEED, breath="")
sun_B.add_asana(Warrior1(), "i")
sun_B.add_asana(LowLunge(), "o")
sun_B.add_asana(LegToChest(), time=1.5/SPEED, breath="")
sun_B.add_asana(Plank(), "i")
sun_B.add_asana(Chaturanga(), "o")
sun_B.add_asana(UpDog(), "i")
sun_B.add_asana(DownDog(), "oioioioioio")
sun_B.add_asana(LegToChest(), time=1.5/SPEED, breath="")
sun_B.add_asana(LowLunge(), "i")
sun_B.add_asana(ForwardFold(), "o")
sun_B.add_asana(Chair(), "i")
sun_B.add_asana(Standing(), "o")


ashtanga = Sequence("Ashtanga Yoga")
# ashtanga.append_sequence(meditation)
ashtanga.append_sequence(catcow)
ashtanga.append_sequence(vinyasa_cat_to_stand)
for i in range(4):
    ashtanga.append_sequence(sun_A)
for i in range(4):
    ashtanga.append_sequence(sun_B)

ashtanga.add_asana(Standing(), "o")
