"""
aoc y2015 day 1
https://adventofcode.com/2015/day/1
"""
import re


def d1parse(data):
    """
    As data is a list of all the lines in the file, and the file only contains 1 line
    return the first element of data as data
    """
    return data[0]


def d1p1_old(data):
    """
    Old basic version of the code
    """
    result = 0
    for c in data:
        if c == '(':
            result += 1
        else:
            result -= 1

    return result


def d1p1(data):
    """
    part 1
    """
    pluses = data.count('(')
    minuses = len(data) - pluses
    return pluses - minuses


def d1p2(data):
    """
    part 2
    """
    result = 0
    index = 0
    for c in data:
        if result == -1:
            return index

        if c == '(':
            result += 1

        else:
            result -= 1
        index += 1
