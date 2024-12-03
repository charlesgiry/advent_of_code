"""
aoc y2015 day 17
https://adventofcode.com/2015/day/17
"""
from itertools import combinations


def d17parse(data):
    """
    parse
    """
    return [int(i) for i in data]


def d17p1(data):
    """
    part 1
    """
    result = 0
    for i in range(len(data)):
        for containers in combinations(data, i):
            if sum(containers) == 150:
                result += 1
    return result


def d17p2(data):
    """
    part 2
    """
    lens = dict()
    for i in range(len(data)):
        for containers in combinations(data, i):
            if sum(containers) == 150:
                len_containers = len(containers)
                if len_containers not in lens:
                    lens[len_containers] = []
                lens[len_containers].append(containers)
    return len(lens[min(lens.keys())])
