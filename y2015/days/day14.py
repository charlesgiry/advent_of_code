"""
aoc y2015 day 14
https://adventofcode.com/2015/day/14
"""


class Reindeer:
    name: str
    speed: int
    fly_duration: int
    rest_duration: int
    counter: int
    km_flown: int
    points: int
    __period: int

    def __init__(self, name: str, speed: int, fly_duration: int, rest_duration: int):
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration
        self.counter = 0
        self.km_flown = 0
        self.points = 0
        self.__period = self.fly_duration + self.rest_duration

    def race(self):
        action = self.counter % self.__period
        if action < self.fly_duration:
            self.km_flown += self.speed
        self.counter += 1

    def reset(self):
        self.counter = 0
        self.km_flown = 0
        self.points = 0

    def __lt__(self, other):
        if isinstance(other, Reindeer):
            return self.km_flown < other.km_flown
        else:
            return NotImplemented


def d14parse(data):
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
    This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy.
    Santa would like to know which of his reindeer is fastest, and so he has them race.
    Reindeer can only either be flying (always at their top speed) or resting (not moving at all),
    and always spend whole seconds in either state.

    For example, suppose you have the following Reindeer:
        Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

    After one second, Comet has gone 14 km, while Dancer has gone 16 km.
    After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
    On the eleventh second, Comet begins resting (staying at 140 km),
    and Dancer continues on for a total distance of 176 km.
    On the 12th second, both reindeer are resting. They continue to rest until the 138th second,
    when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.
    In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km
    (poor Dancer has only gotten 1056 km by that point).
    So, in this situation, Comet would win (if the race ended at 1000 seconds).

    Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds,
    what distance has the winning reindeer traveled?
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
    Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.
    Instead, at the end of each second, he awards one point to the reindeer currently in the lead.
    (If there are multiple reindeer tied for the lead, they each get one point.)
    He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

    Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point.
    He stays in the lead until several seconds into Comet's second burst:
    after the 140th second, Comet pulls into the lead and gets his first point.
    Of course, since Dancer had been in the lead for the 139 seconds before that,
    he has accumulated 139 points by the 140th second.

    After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312.
    So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).
    Again given the descriptions of each reindeer (in your puzzle input),
    after exactly 2503 seconds, how many points does the winning reindeer have?
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
