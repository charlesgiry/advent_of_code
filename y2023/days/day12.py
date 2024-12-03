"""
aoc y2023 day 12
https://adventofcode.com/2023/day/12
"""
from copy import copy
from functools import cache


def d12parse(data):
    """
    parse
    """
    records = []
    for line in data:
        split_line = line.split()
        springs = split_line[0]
        groups = [int(x) for x in split_line[1].split(',')]
        records.append((springs, groups))

    return records


def count_possibilities(springs, groups):
    """
    count the numer of correct puzzles where
    replacing ? by either . or # would give the correct number of groups
    """
    def valid_group(current, length):
        """
        Check whether the substring starting at current and ending at current + length
        is a group composed by #s and ?s
        """
        return '.' not in springs[current:current + length] \
            and current + length <= len(springs) \
            and (current + length == len(springs) or springs[current + length] in ['.', '?'])

    @cache
    def internal(current, current_group):
        """
        cached recursive exploration of the string to go faster
        """
        if current_group == len(groups):
            return int('#' not in springs[current:])

        if current >= len(springs):
            return 0

        spring = springs[current]
        group = groups[current_group]
        if spring == '#':
            if valid_group(current, group):
                return internal(current + group + 1, current_group + 1)
            else:
                return 0

        elif spring == '?':
            if valid_group(current, group):
                return internal(current + group + 1, current_group + 1) + internal(current + 1, current_group)

        return internal(current+1, current_group)
    return internal(0, 0)


def d12p1(data):
    """
    part 1
    """
    result = 0
    for springs, groups in data:
        result += count_possibilities(springs, groups)
    return result


def d12p2(data):
    """
    part 2
    """
    result = 0
    for springs, groups in data:
        # unfold the values
        springs = '?'.join(springs for i in range(5))
        g = copy(groups)
        groups = []
        for i in range(5):
            groups += g

        # get the result
        result += count_possibilities(springs, groups)

    return result
