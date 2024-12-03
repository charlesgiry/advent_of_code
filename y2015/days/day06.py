"""
aoc y2015 day 6
https://adventofcode.com/2015/day/6
"""
from numpy import zeros, bool_, int_


def d6parse(data):
    """
    parse
    """
    result = []
    i = 0
    for line in data:
        split_line = line.split()

        if split_line[0] == 'turn':
            if split_line[1] == 'on':
                action = 1
            else:
                action = -1
            split_line = split_line[2::2]
        else:
            action = 2
            split_line = split_line[1::2]

        from_ = [int(i) for i in split_line[0].split(',')]
        to_ = [int(i) for i in split_line[1].split(',')]

        current_line = (action, from_, to_)
        result.append(current_line)
    return result


def d6p1(data):
    """
    part 1
    """
    grid = zeros((1000, 1000), dtype=bool_)
    for line in data:
        action, from_, to_ = line
        from_y, from_x = from_[0], from_[1]
        to_y, to_x = to_[0] + 1, to_[1] + 1
        if action == -1:
            grid[from_y:to_y, from_x:to_x] = False
        elif action == 1:
            grid[from_y:to_y, from_x:to_x] = True
        else:
            grid[from_y:to_y, from_x:to_x] = grid[from_y:to_y, from_x:to_x] ^ 1

    result = 0
    for line in grid:
        for light in line:
            if light:
                result += 1
    return result


def d6p1_old(data):
    """
    old version using lists instead of numpy
    """
    grid = [
        [False for _ in range(1000)] for _ in range(1000)
    ]

    for line in data:
        action, from_, to_ = line
        from_y, from_x = from_[0], from_[1]
        to_y, to_x = to_[0] + 1, to_[1] + 1

        for y in range(from_y, to_y):
            for x in range(from_x, to_x):
                if action == 1:
                    grid[y][x] = True
                elif action == 2:
                    grid[y][x] = not grid[y][x]
                else:
                    grid[y][x] = False

    result = 0
    for line in grid:
        for light in line:
            if light:
                result += 1

    return result


def d6p2(data):
    """
    part 2
    """
    grid = zeros((1000, 1000), dtype=int_)
    for line in data:
        action, from_, to_ = line
        from_y, from_x = from_[0], from_[1]
        to_y, to_x = to_[0] + 1, to_[1] + 1

        grid[from_y:to_y, from_x:to_x] += action
        grid[grid < 0] = 0

    result = 0
    for line in grid:
        for light in line:
            result += light
    return result


def d6p2_old(data):
    """
    old less performant version of the code
    """
    grid = [
        [0 for _ in range(1000)] for _ in range(1000)
    ]
    for line in data:
        action, from_, to_ = line
        from_y, from_x = from_[0], from_[1]
        to_y, to_x = to_[0] + 1, to_[1] + 1

        for y in range(from_y, to_y):
            for x in range(from_x, to_x):
                grid[y][x] += action
                if grid[y][x] < 0:
                    grid[y][x] = 0
    result = 0
    for line in grid:
        for light in line:
            result += light
    return result
