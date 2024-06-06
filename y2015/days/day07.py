"""
aoc y2015 day 7
https://adventofcode.com/2015/day/7
"""
from functools import cache

# Operations as a global variable to be usable in cached explore function
operations = {}


def d7parse(data):
    for line in data:
        operation, result = line.split(' -> ')
        operations[result] = operation.split()
    return operations


@cache
def explore(value):
    if value.isdigit():
        return int(value)

    operation = operations[value]
    if len(operation) == 1:
        result = explore(operation[0])
    else:
        operator = operation[-2]
        if operator == 'AND':
            result = explore(operation[0]) & explore(operation[2])
        elif operator == 'OR':
            result = explore(operation[0]) | explore(operation[2])
        elif operator == 'RSHIFT':
            result = explore(operation[0]) >> explore(operation[2])
        elif operator == 'LSHIFT':
            result = explore(operation[0]) << explore(operation[2])
        else:
            result = explore(operation[1]) ^ 0xffff

    return result


def d7p1(data):
    return explore('a')


def d7p2(data):
    result = explore('a')
    operations['b'] = [str(result)]
    explore.cache_clear()
    return explore('a')
