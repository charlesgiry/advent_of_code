"""
aoc y2024 day 1
https://adventofcode.com/2024/day/1
"""

def d1parse(data):
    """
    parse
    """
    results = {
        'left': [],
        'right': []
    }
    for line in data:
        split_line = line.split()
        results['left'].append(int(split_line[0]))
        results['right'].append(int(split_line[1]))
    return results


def d1p1(data):
    """
    part 1
    """
    left = data['left']
    right = data['right']

    left.sort()
    right.sort()

    result = 0
    for i in range(len(left)):
        r = sorted([
            left[i],
            right[i]
        ])
        result += (r[1] - r[0])

    return result


def d1p2(data):
    """
    part 2
    """
    number = {}

    for i in data['right']:
        if i not in number:
            number[i] = 0
        number[i] += 1

    result = 0
    for i in data['left']:
        if i in number:
            result += (i * number[i])

    return result
