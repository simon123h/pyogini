from asanas import *
# todo: support nested sequences


class Sequence:

    def __init__(self, name):
        self.name = name
        self.asanas = []
        self.timing = []

    def add(self, asana, time=15):
        self.asanas.append(asana)
        self.timing.append(time)

    def get_asana(self, time):
        time = time % self.total_time()
        index = -1
        while time >= 0:
            index += 1
            time -= self.timing[index]
        return self.asanas[index]

    def total_time(self):
        return sum(self.timing)


sun_A = Sequence("Sun Salutation A")
sun_A.add(Standing(), 2)
sun_A.add(UpwardSalute(), 2)
sun_A.add(ForwardFold(), 2)
sun_A.add(HalfwayLift(), 2)
sun_A.add(Lunge(), 2)
sun_A.add(Plank(), 2)
sun_A.add(Chaturanga(), 2)
sun_A.add(UpDog(), 2)
sun_A.add(DownDog(), 2)
sun_A.add(Lunge(), 2)
sun_A.add(ForwardFold(), 2)
