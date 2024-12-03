"""
aoc y2024 day 03
https://adventofcode.com/2024/day/3
"""
from re import compile


def d3p1(data):
    """
    part 1
    """
    result = 0
    regexp = compile(r'mul\((\d+),(\d+)\)')
    for line in data:
        found = regexp.findall(line)
        for elem in found:
            result += (int(elem[0]) * int(elem[1]))

    return result

def d3p2(data):
    """
    part 2
    """
    result = 0
    regexp = compile(r"(mul\((\d+),(\d+)\)|do(n't)?\(\))")
    keep = True
    for line in data:
        found = regexp.findall(line)
        for elem in found:
            if elem[0] == 'do()':
                keep = True
            elif elem[0] == "don't()":
                keep = False
            elif keep:
                result += (int(elem[1]) * int(elem[2]))
    return result
