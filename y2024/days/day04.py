"""
aoc y2024 day 04
https://adventofcode.com/2024/day/4
"""


def d4parse(data):
    """
    Add bounds for simpler checks
    surround puzzles with dots
    """
    result = ['.' * (len(data[0]) + 2) ]
    for line in data:
        result.append(f'.{line}.')
    result.append('.' * (len(data[0]) + 2))

    return result


def d4p1(data):
    """
    part 1
    """
    size_y = len(data)
    size_x = len(data[0])
    result = 0
    for y in range(1, size_y - 1):
        for x in range(1, size_x - 1):
            if data[y][x] == 'X':
                # left - right
                if data[y][x+1] == 'M' and data[y][x+2] == 'A' and data[y][x+3] == 'S':
                    result += 1

                # right - left
                if data[y][x-1] == 'M' and data[y][x-2] == 'A' and data[y][x-3] == 'S':
                    result += 1

                # top - bottom
                if data[y+1][x] == 'M' and data[y+2][x] == 'A' and data[y+3][x] == 'S':
                    result += 1

                # bottom - top
                if data[y-1][x] == 'M' and data[y-2][x] == 'A' and data[y-3][x] == 'S':
                    result += 1

                # diag top right - bottom left
                if data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S':
                    result += 1

                # diag bottom left - top right
                if data[y-1][x-1] == 'M' and data[y-2][x-2] == 'A' and data[y-3][x-3] == 'S':
                    result += 1

                # diag top left - bottom right
                if data[y+1][x-1] == 'M' and data[y+2][x-2] == 'A' and data[y+3][x-3] == 'S':
                    result += 1

                # diag bottom right - top left
                if data[y-1][x+1] == 'M' and data[y-2][x+2] == 'A' and data[y-3][x+3] == 'S':
                    result += 1
    return result


def d4p2(data):
    """
    part 2
    """
    result = 0
    size_y = len(data)
    size_x = len(data[0])
    for y in range(1, size_y - 1):
        for x in range(1, size_x - 1):
            if data[y][x] == 'A':
                if data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S':
                    if data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S':
                        result += 1
                    elif data[y+1][x-1] == 'S' and data[y-1][x+1] == 'M':
                        result += 1

                if data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M':
                    if data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S':
                        result += 1
                    elif data[y+1][x-1] == 'S' and data[y-1][x+1] == 'M':
                        result += 1
    return result
