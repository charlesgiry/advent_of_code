"""
aoc y2015 day 6
https://adventofcode.com/2015/day/6
"""
from numpy import zeros, bool_, int_


def d6parse(data):
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
    Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.
    Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

    Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

    To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

    For example:
    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
    After following the instructions, how many lights are lit?
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
    You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
    The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.
    The phrase turn on actually means that you should increase the brightness of those lights by 1.

    The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
    The phrase toggle actually means that you should increase the brightness of those lights by 2.
    What is the total brightness of all lights combined after following Santa's instructions?

    For example:
    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.
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
