"""
aoc y2015 day 20
https://adventofcode.com/2015/day/20
"""
from numpy import zeros


def d20parse(data):
    """
    parse
    """
    return int(data[0])


def d20p1(data):
    """
    part 1
    """
    houses = zeros(data, dtype=int)

    # Since all elves give at least 10 gift, it is expected to find the result before i reaches data divided by 10
    upper_bound = data // 10

    for i in range(1, data+1):
        current_val = i * 10
        houses[i-1:upper_bound:i] += current_val
        if houses[i-1] >= data:
            return i

    return None


def d20p2(data):
    """
    part 2
    """
    houses = zeros(data, dtype=int)

    for i in range(1, data+1):
        current_val = i * 11
        houses[i-1:(i*50):i] += current_val

        if houses[i-1] >= data:
            return i
    return None
