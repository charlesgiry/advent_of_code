"""
aoc y2024 day 02
https://adventofcode.com/2024/day/2
"""
from operator import gt, lt


def d2parse(data):
    """
    parse
    """
    results = []
    for line in data:
        split_line = line.split()
        results.append([int(x) for x in split_line])
    return results


def monotonic(line: list[int]):
    """
    Check that all the elements of a list follow the same order from first to last element
    """
    function = gt if line[0] > line[1] else lt
    for i in range(len(line) - 1):
        if not (function(line[i], line[i+1])):
            return False
    return True


def adjacent_difference(line: list[int]):
    """
    Check that all the values of the elements of a list are within 1 to 3 of their neighbors
    """
    for i in range(len(line) - 1):
        if not (1 <= abs(line[i] - line[i + 1]) <= 3):
            return False
    return True


def valid(line: list[int]):
    """
    Check both rules above
    """
    return monotonic(line) and adjacent_difference(line)


def d2p1(data):
    """
    part 1
    """
    result = 0
    for line in data:
        if valid(line):
            result += 1
    return result


def remove(line: list[int], pos: int):
    """
    return a list with the element at position pos removed
    """
    if pos == 0:
        return line[1:]
    if pos == len(line) - 1:
        return line[:-1]
    return line[:pos] + line[pos+1:]


def index_of_fail(line):
    """
    return the index of the elements that do not follow the defined rules
    """
    result = set()

    function = gt if line[0] > line[1] else lt
    for i in range(len(line) - 1):
        if not (function(line[i], line[i+1])):
            result.add(i)
        if not (1 <= abs(line[i] - line[i + 1]) <= 3):
            result.add(i)

    return result


def d2p2(data):
    """
    part 2
    """
    result = 0
    for line in data:
        fails = index_of_fail(line)
        if not fails:
            result += 1
        else:
            for i in fails:
                if valid(remove(line, i)):
                    result += 1
                    break
                if i >= 1 and valid(remove(line, i-1)):
                    result += 1
                    break
                if i < len(line) -1 and valid(remove(line, i+1)):
                    result += 1
                    break
    return result


def d2p2_old(data):
    """
    brute force solution
    """
    result = 0
    for line in data:
        if valid(line):
            result += 1
        else:
            for i in range(len(line)):
                if valid(remove(line, i)):
                    result += 1
                    break
    return result
