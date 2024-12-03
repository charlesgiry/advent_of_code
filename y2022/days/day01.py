"""
aoc y2022 day 1
https://adventofcode.com/2022/day/1
"""


def d1parse(data):
    """
    parse
    """
    elves = []
    elf = []
    for line in data:
        if line != '':
            elf.append(int(line))
        else:
            elves.append(elf.copy())
            elf = []
    return elves


def d1p1(data):
    """
    part 1
    """
    max = 0
    for elf in data:
        s = sum(elf)
        if s >= max:
            max = s
    return max

def d1p2(data):
    """
    part 2
    """
    max = [0, 0, 0]
    for elf in data:
        s = sum(elf)

        if s >= max[-1]:
            max.append(s)
            max.pop(0)

        elif s >= max[1]:
            max.insert(2, s)
            max.pop(0)

        elif s >= max[0]:
            max[0] = s

    return sum(max)


def d1p2_old(data):
    """

    """
    elves = []
    for elf in data:
        s = sum(elf)
        elves.append(s)

    elves.sort()
    return sum(elves[-3:])
