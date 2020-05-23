from asanas import *
# TODO: support nested sequences


class Sequence:

    def __init__(self, name):
        self.name = name
        self.asanas = []

    def add(self, asana, time=None, breath=None):
        self.asanas.append(asana)
        if time is None:
            time = 2 if breath is None else 4 * len(breath)
        asana.time = time
        if breath is not None:
            asana.breath = breath

    def get_asana(self, time):
        time = time % self.total_time()
        index = -1
        while time >= 0:
            index += 1
            time -= self.asanas[index].time
        return self.asanas[index], -time

    def total_time(self):
        return sum([a.time for a in self.asanas])


sun_A = Sequence("Sun Salutation A")
sun_A.add(Standing(), breath="io")
sun_A.add(UpwardSalute(), breath="i")
sun_A.add(ForwardFold(), breath="o")
sun_A.add(HalfwayLift(), breath="i")
sun_A.add(Lunge(), breath="o")
sun_A.add(Plank(), breath="i")
sun_A.add(Chaturanga(), breath="o")
sun_A.add(UpDog(), breath="i")
sun_A.add(DownDog(), breath="oioio")
sun_A.add(Lunge(), breath="i")
sun_A.add(ForwardFold(), breath="o")
