"""
aoc y2015 day 10
https://adventofcode.com/2015/day/10
"""
def d10parse(data):
    return data[0]


def look_and_say(start):
    current = ''
    current_number = 0

    result = ''
    for c in start:
        if current != c:
            if current_number > 0:
                result += f'{current_number}{current}'
            current = c
            current_number = 1
        else:
            current_number += 1

    if current_number > 0:
        result += f'{current_number}{current}'

    return result


def d10p1(data):
    current = data
    for i in range(40):
        current = look_and_say(current)
    return len(current)


def d10p2(data):
    current = data
    for i in range(50):
        current = look_and_say(current)
    return len(current)
