"""
aoc y2015 day 5
https://adventofcode.com/2015/day/5
"""
from re import compile


def d5p1(data):
    """
    part 1
    """
    result = 0
    rule1 = compile(r'[aeiou]')
    rule2 = compile(r'(.)\1')
    rule3 = compile(r'(ab|cd|pq|xy)')

    for line in data:
        cond1 = len(rule1.findall(line)) >= 3
        cond2 = bool(rule2.search(line))
        cond3 = bool(rule3.search(line))
        if cond1 and cond2 and (not cond3):
            result += 1

    return result


def d5p2(data):
    """
    part 2
    """
    result = 0
    rule1 = compile(r'([a-z]{2}).*\1')
    rule2 = compile(r'([a-z]).\1')

    for line in data:
        cond1 = bool(rule1.search(line))
        cond2 = bool(rule2.search(line))
        if cond1 and cond2:
            result += 1

    return result
