"""
aoc y2015 day 7
https://adventofcode.com/2015/day/7
"""
operations = {}
results = {}


def d7parse(data):
    for line in data:
        operation, result = line.split(' -> ')
        operations[result] = operation.split()
    return operations


def explore(value):
    if value.isdigit():
        return int(value)

    if value in results:
        return results[value]

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

    results[value] = result
    return result


def d7p1(data):
    return explore('a')


def d7p2(data):
    result = explore('a')
    operations['b'] = [str(result)]
    results.clear()
    return explore('a')
