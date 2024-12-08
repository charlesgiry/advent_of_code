"""
aoc y2024 day 08
https://adventofcode.com/2024/day/8
"""
from numpy import array, unique, argwhere

from itertools import combinations


def d8parse(data):
    """
    parse
    """
    result = array([list(line) for line in data], dtype='U1')
    return result


def d8p1(data):
    """
    part 1
    """
    antennas = unique(data[data != '.'])
    antinodes = set()
    for antenna in antennas:
        positions = argwhere(data == antenna)
        lines = combinations(positions, 2)

        for point1, point2 in lines:
            diff_y = point2[0] - point1[0]
            diff_x = point2[1] - point1[1]
            antinode_1 = (point1[0] - diff_y, point1[1] - diff_x)
            antinode_2 = (point2[0] + diff_y, point2[1] + diff_x)

            if 0 <= antinode_1[0] < data.shape[0] and 0 <= antinode_1[1] < data.shape[1]:
                antinodes.add(antinode_1)
            if 0 <= antinode_2[0] < data.shape[0] and 0 <= antinode_2[1] < data.shape[1]:
                antinodes.add(antinode_2)

    return len(antinodes)


def d8p2(data):
    """
    part 2
    """
    antennas = unique(data[data != '.'])
    antinodes = set()
    for antenna in antennas:
        positions = argwhere(data == antenna)
        lines = combinations(positions, 2)

        for point1, point2 in lines:
            diff_y = point2[0] - point1[0]
            diff_x = point2[1] - point1[1]

            y, x = point1
            antinodes.add((y, x))

            # line point2 -> point1
            while 0 <= y < data.shape[0] and 0 <= x < data.shape[1]:
                antinodes.add((y, x))
                y -= diff_y
                x -= diff_x

            # line point1 -> point2
            y, x = point1
            while 0 <= y < data.shape[0] and 0 <= x < data.shape[1]:
                antinodes.add((y, x))
                y += diff_y
                x += diff_x


    return len(antinodes)
