"""

"""
from pprint import pprint

def d1parse(data):
    """

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
    max = 0
    for elf in data:
        s = sum(elf)
        if s >= max:
            max = s
    print(max)

def d1p2(data):
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
    elves = []
    for elf in data:
        s = sum(elf)
        elves.append(s)

    elves.sort()
    return sum(elves[-3:])


if __name__ == '__main__':
    with open('../data/day01.txt') as f:
        data = f.read().splitlines()

    parsed_data = d1parse(data)
    d1p1(parsed_data)

    for i in range(100000):
        d1p2(parsed_data)
        d1p2_old(parsed_data)
