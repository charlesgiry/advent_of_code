"""
aoc y2015 day 16
https://adventofcode.com/2015/day/16
"""
from re import compile

class Sue:
    """
        children: 3
        cats: 7
        samoyeds: 2
        pomeranians: 3
        akitas: 0
        vizslas: 0
        goldfish: 5
        trees: 3
        cars: 2
        perfumes: 1
    """
    id: int
    children: int
    cats: int
    samoyeds: int
    pomeranians: int
    akitas: int
    vizslas: int
    goldfish: int
    trees: int
    cars: int
    perfumes: int

    def __init__(self):
        self.id = 0
        self.children = -1
        self.cats = -1
        self.samoyeds = -1
        self.pomeranians = -1
        self.akitas = -1
        self.vizslas = -1
        self.goldfish = -1
        self.trees = -1
        self.cars = -1
        self.perfumes = -1

    def eq_part1(self, other):
        for key, value in self.__dict__.items():
            if key != 'id':
                if value >= 0 and value != other.__dict__[key]:
                    return False
        return True

    def eq_part2(self, other):
        for key, value in self.__dict__.items():
            if key != 'id':
                if key == 'cats' or key == 'trees':
                    if value >= 0 and value < other.__dict__[key]:
                        return False

                elif key == 'pomeranians' or key == 'goldfish':
                    if value >= 0 and value > other.__dict__[key]:
                        return False

                else:
                    if value >= 0 and value != other.__dict__[key]:
                        return False
        return True


def d16parse(data):
    child_pattern = compile(r'children: (\d+)')
    cat_pattern = compile(r'cats: (\d+)')
    samoyed_pattern = compile(r'samoyeds: (\d+)')
    pomeranian_pattern = compile(r'pomeranians: (\d+)')
    akita_pattern = compile(r'akitas: (\d+)')
    vizsla_pattern = compile(r'vizslas: (\d+)')
    goldfish_pattern = compile(r'goldfish: (\d+)')
    tree_pattern = compile(r'trees: (\d+)')
    car_pattern = compile(r'cars: (\d+)')
    perfume_pattern = compile(r'perfumes: (\d+)')

    result = []
    i = 1
    for line in data:
        aunt = Sue()
        aunt.id = i
        aunt.children = -1
        aunt.cats = -1
        aunt.samoyeds = -1
        aunt.pomeranians = -1
        aunt.akitas = -1
        aunt.vizslas = -1
        aunt.goldfish = -1
        aunt.trees = -1
        aunt.cars = -1
        aunt.perfumes = -1

        match = child_pattern.search(line)
        if match:
            aunt.children = int(match.group(1))

        match = cat_pattern.search(line)
        if match:
            aunt.cats = int(match.group(1))

        match = samoyed_pattern.search(line)
        if match:
            aunt.samoyeds = int(match.group(1))

        match = pomeranian_pattern.search(line)
        if match:
            aunt.pomeranians = int(match.group(1))

        match = akita_pattern.search(line)
        if match:
            aunt.akitas = int(match.group(1))

        match = vizsla_pattern.search(line)
        if match:
            aunt.vizslas = int(match.group(1))

        match = goldfish_pattern.search(line)
        if match:
            aunt.goldfish = int(match.group(1))

        match = tree_pattern.search(line)
        if match:
            aunt.trees = int(match.group(1))

        match = car_pattern.search(line)
        if match:
            aunt.cars = int(match.group(1))

        match = perfume_pattern.search(line)
        if match:
            aunt.perfumes = int(match.group(1))

        result.append(aunt)
        i += 1

    return result


# The aunt you're looking for
searching_for = Sue()
searching_for.children = 3
searching_for.cats = 7
searching_for.samoyeds = 2
searching_for.pomeranians = 3
searching_for.akitas = 0
searching_for.vizslas = 0
searching_for.goldfish = 5
searching_for.trees = 3
searching_for.cars = 2
searching_for.perfumes = 1


def d16p1(data):
    """
    Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card.
    However, there's a small problem: she signed it "From, Aunt Sue".
    You have 500 Aunts named "Sue".
    So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue
    (which you conveniently number 1 to 500, for sanity) gave you the gift.
    You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine!
    Just what you wanted. Or needed, as the case may be.

    The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample,
    as well as how many distinct kinds of those compounds there are.
    According to the instructions, these are what the MFCSAM can detect:
        children, by human DNA age analysis.
        cats. It doesn't differentiate individual breeds.
        Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
        goldfish. No other kinds of fish.
        trees, all in one group.
        cars, presumably by exhaust or gasoline or something.
        perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

    In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM.
    It beeps inquisitively at you a few times and then prints out a message on ticker tape:
        children: 3
        cats: 7
        samoyeds: 2
        pomeranians: 3
        akitas: 0
        vizslas: 0
        goldfish: 5
        trees: 3
        cars: 2
        perfumes: 1
    You make a list of the things you can remember about each Aunt Sue.
    Things missing from your list aren't zero - you simply don't remember the value.

    What is the number of the Sue that got you the gift?
    """
    for aunt in data:
        if aunt.eq_part1(searching_for):
            return aunt.id


def d16p2(data):
    """
    As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye.
    Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values -
        some of them indicate ranges.
    In particular,
        the cats and trees readings indicates that there are greater than that many
        (due to the unpredictable nuclear decay of cat dander and tree pollen),
        while the pomeranians and goldfish readings indicate that there are fewer than that many
        (due to the modial interaction of magnetoreluctance).
    What is the number of the real Aunt Sue?
    """
    for aunt in data:
        if aunt.eq_part2(searching_for) and not aunt.eq_part1(searching_for):
            return aunt.id
