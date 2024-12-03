"""
aoc y2015 day 4
https://adventofcode.com/2015/day/4
"""
from hashlib import md5


def d4parse(data):
    """
    As data is a list of all the lines in the file, and the file only contains 1 line
    return the first element of data as data
    """
    return data[0]


def findhex(data, target):
    """

    """
    i = 0
    result = md5(f'{data}{i}'.encode()).hexdigest()
    while not result.startswith(target):
        i += 1
        result = md5(f'{data}{i}'.encode()).hexdigest()
    return i


def d4p1(data):
    """
    part 1
    """
    return findhex(data, '00000')


def d4p2(data):
    """
    part 2
    """
    return findhex(data, '000000')
