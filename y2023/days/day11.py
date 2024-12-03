"""
aoc y2023 day 11
https://adventofcode.com/2023/day/11
"""
from itertools import combinations


def d11parse(data):
    """
    parse
    """
    max_y = len(data)
    max_x = len(data[0])

    # find the cosmic growth lines
    add_lines = []
    for i in range(len(data)):
        line = data[i]
        if '#' not in line:
            add_lines.append(i)

    # find the cosmic growth columns
    add_rows = []
    for i in range(len(data[0])):
        hash_number = 0
        for j in range(len(data)):
            if data[j][i] == '#':
                hash_number += 1

        if hash_number == 0:
            add_rows.append(i)

    # create a list containing all galaxy pairs
    galaxies = set()
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == '#':
                galaxies.add((y, x))

    galaxy_pairs = set(combinations(galaxies, 2))

    return (galaxy_pairs, add_lines, add_rows)


def get_result(galaxy_pairs, add_lines, add_rows, galaxy_growth):
    """
    calculate the expected result by taking into account galaxy growth
    """
    result = 0
    for pair in galaxy_pairs:
        p = iter(pair)
        galaxy1 = next(p)
        galaxy2 = next(p)

        y1, x1 = galaxy1
        y2, x2 = galaxy2

        xmax = max(x1, x2)
        ymax = max(y1, y2)
        xmin = min(x1, x2)
        ymin = min(y1, y2)

        distance = xmax + ymax - xmin - ymin
        for y in add_lines:
            if ymin < y < ymax:
                distance += galaxy_growth - 1
        for x in add_rows:
            if xmin < x < xmax:
                distance += galaxy_growth - 1

        result += distance

    return result


def d11p1(data):
    """
    part 1
    """
    galaxy_pairs, add_lines, add_rows = data
    return get_result(galaxy_pairs, add_lines, add_rows, 2)


def d11p2(data):
    """
    part 2
    """
    galaxy_pairs, add_lines, add_rows = data
    return get_result(galaxy_pairs, add_lines, add_rows, 1000000)
