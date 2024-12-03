"""
aoc y2023 day 2
https://adventofcode.com/2023/day/2
"""
from re import compile

# prepare regexp to find all the colored balls in a line
blue_regexp = compile(r'\d+ blue')
green_regexp = compile(r'\d+ green')
red_regexp = compile(r'\d+ red')


def d2parse(data):
    """
    parse
    """
    lines = []
    for line in data:
        id, blue, green, red = parse_game(line)
        lines.append([id, blue, green, red])
    return lines


def parse_game(line):
    """

    """
    id = int(line.split(':')[0].split()[1])

    b = blue_regexp.findall(line)
    blue = []
    for eb in b:
        blue.append(int(eb.split()[0]))

    g = green_regexp.findall(line)
    green = []
    for eg in g:
        green.append(int(eg.split()[0]))

    r = red_regexp.findall(line)
    red = []
    for er in r:
        red.append(int(er.split()[0]))

    return id, blue, green, red


def d2p1(data):
    """
    part 1
    """
    result = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    for game in data:
        id, blue, green, red = game
        try:
            if max(blue) > max_blue:
                pass
            elif max(green) > max_green:
                pass
            elif max(red) > max_red:
                pass
            else:
                result += id
        except ValueError:
            pass

    return result


def d2p2(data):
    """
    part 2
    """
    result = 0
    for game in data:
        _, blue, green, red = game
        max_red = max(blue)
        max_green = max(green)
        max_blue = max(red)

        cube_power = max_red * max_green * max_blue
        result += cube_power

    return result
