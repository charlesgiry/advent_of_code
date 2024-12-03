"""
aoc y2015 day 18
https://adventofcode.com/2015/day/18
"""
from numpy import array, pad, count_nonzero


def d18parse(data):
    """
    parse
    """
    return [
        [True if x == '#' else False for x in list(l)] for l in data
    ]


def count_neighbours_old(y, x, grid):
    """

    """
    lit_around = 0
    for i in range(max(0, y - 1), min(len(grid), y + 2)):
        for j in range(max(0, x - 1), min(len(grid[0]), x + 2)):
            if grid[i][j] and ((i != y) or (j != x)):
                lit_around += 1
    return lit_around


def d18p1_old(data):
    """

    """
    current = data
    next_ = [[False] * len(data[0]) for _ in range(len(data))]

    for _ in range(100):
        for i in range(len(data)):
            for j in range(len(data[0])):
                on = current[i][j]
                neighbours = count_neighbours_old(i, j, current)
                if on:
                    if neighbours in [2, 3]:
                        next_[i][j] = True
                    else:
                        next_[i][j] = False
                else:
                    if neighbours == 3:
                        next_[i][j] = True
                    else:
                        next_[i][j] = False
        next_, current = current, next_

    result = 0
    for line in current:
        for elem in line:
            if elem:
                result += 1
    return result


def count_neighbours(grid, current):
    """

    """
    result = count_nonzero(grid)
    if current:
        result -= 1 if result > 1 else 0
    return result


def step(grid):
    """

    """
    result = grid.copy()
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            cell = grid[y][x]
            neighbours_grid = grid[y-1: y+2, x-1: x+2]
            neighbours = count_neighbours(neighbours_grid, cell)
            if cell:
                result[y, x] = ((neighbours == 2) or (neighbours == 3))
            else:
                result[y, x] = (neighbours == 3)

    return result


def d18p1(data):
    """
    part 1
    """
    current = array([[x for x in y] for y in data], dtype=bool)
    current = pad(current, pad_width=1, mode='constant', constant_values=False)
    for _ in range(100):
        current = step(current)
    return count_nonzero(current)


def d18p2(data):
    """
    part 2
    """
    current = array([[x for x in y] for y in data], dtype=bool)
    current = pad(current, pad_width=1, mode='constant', constant_values=False)

    for _ in range(100):
        current = step(current)
        current[1, 1] = True
        current[1, -2] = True
        current[-2, 1] = True
        current[-2, -2] = True

    return count_nonzero(current)
