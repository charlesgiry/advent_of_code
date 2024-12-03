"""
aoc y2015 day 14
https://adventofcode.com/2015/day/14
"""


class Reindeer:
    """

    """
    name: str
    speed: int
    fly_duration: int
    rest_duration: int
    counter: int
    km_flown: int
    points: int
    __period: int

    def __init__(self, name: str, speed: int, fly_duration: int, rest_duration: int):
        """

        """
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration
        self.counter = 0
        self.km_flown = 0
        self.points = 0
        self.__period = self.fly_duration + self.rest_duration

    def race(self):
        """

        """
        action = self.counter % self.__period
        if action < self.fly_duration:
            self.km_flown += self.speed
        self.counter += 1

    def reset(self):
        """

        """
        self.counter = 0
        self.km_flown = 0
        self.points = 0

    def __lt__(self, other):
        """

        """
        if isinstance(other, Reindeer):
            return self.km_flown < other.km_flown
        else:
            return NotImplemented


def d14parse(data):
    """
    parse
    """
    reindeers = []
    for line in data:
        split_line = line.split()
        name = split_line[0]
        speed = int(split_line[3])
        fly_duration = int(split_line[6])
        rest_duration = int(split_line[-2])

        reindeer = Reindeer(name, speed, fly_duration, rest_duration)
        reindeers.append(reindeer)

    return reindeers


def d14p1(data):
    """
    part 1
    """
    for i in range(2503):
        for reindeer in data:
            reindeer.race()

    distances_flown = []
    for reindeer in data:
        distances_flown.append(reindeer.km_flown)

    return max(distances_flown)


def d14p2(data):
    """
    part 2
    """
    for reindeer in data:
        reindeer.reset()

    for i in range(2503):
        for reindeer in data:
            reindeer.race()
        data.sort(reverse=True)
        lead_km = data[0].km_flown
        j = 0
        while data[j].km_flown == lead_km:
            data[j].points += 1
            j += 1

    points = []
    for reindeer in data:
        points.append(reindeer.points)

    return max(points)
