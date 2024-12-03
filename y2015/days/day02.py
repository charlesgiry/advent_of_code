"""
aoc y2015 day 2
https://adventofcode.com/2015/day/2
"""


def d2parse(data):
    """
    parse
    """
    result = []
    for line in data:
        split_line = line.split('x')
        result.append((int(split_line[0]), int(split_line[1]), int(split_line[2])))
    return result


def d2p1(data):
    """
    part 1
    """
    result = 0
    for line in data:
        l, w, h = line

        lw = l * w
        wh = w * h
        hl = h * l

        surface = 2 * (lw + wh + hl)
        surface += min([lw, wh, hl])
        result += surface
    return result


def d2p2(data):
    """
    part 2
    """
    result = 0
    for line in data:
        l, w, h = line
        lw = l + w
        wh = w + h
        hl = h + l
        wrapper = l * w * h
        bow = 2 * min([lw, wh, hl])
        ribbon_len = wrapper + bow

        result += ribbon_len
    return result
