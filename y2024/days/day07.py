"""
aoc y2024 day 07
https://adventofcode.com/2024/day/7
"""
from operator import add, mul


def d7parse(data):
    """
    parse
    """
    result = {}
    for line in data:
        splt = line.split(':')
        result[int(splt[0])] = [int(x) for x in splt[1].split()]

    return result


def product(number, rest, operators, target):
    """
    recursive exploration of pairing every number with every operator from left to right
    """
    if not rest:
        return number == target
    else:
        for operator in operators:
            if product(operator(number, rest[0]), rest[1:], operators, target):
                return True
        return False


def d7p1(data):
    """
    part 1
    """
    operators = [add, mul]
    result = 0

    for target, numbers in data.items():
        if product(numbers[0], numbers[1:], operators, target):
            result += target

    return result


def concat(a, b):
    """
    the definition of the new operator in part 2
    """
    return int(str(a) + str(b))


def d7p2(data):
    """
    part 2
    """
    operators = [add, mul, concat]
    result = 0

    for target, numbers in data.items():
        if product(numbers[0], numbers[1:], operators, target):
            result += target

    return result