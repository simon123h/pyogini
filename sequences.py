from asanas import *
# todo: support nested sequences


class Sequence:

    def __init__(self, name):
        self.name = name
        self.asanas = []
        self.timing = []
        self.current_index = 0
        self.time = 0

    def add(self, asana, time=15):
        self.asanas.append(asana)
        self.timing.append(time)

    def get_asana(self, time):
        index = -1
        while time >= 0:
            index += 1
            time -= self.timing[index]

        return self.asanas[self.current_index]


sun_A = Sequence("Sun Salutation A")
sun_A.add(Standing(), 3)
sun_A.add(UpwardSalute(), 3)
sun_A.add(ForwardFold(), 3)
sun_A.add(Lunge(), 3)
sun_A.add(Plank(), 3)
sun_A.add(Chaturanga(), 3)
sun_A.add(UpDog(), 3)
sun_A.add(DownDog(), 3)
sun_A.add(Lunge(), 3)
sun_A.add(ForwardFold(), 3)
