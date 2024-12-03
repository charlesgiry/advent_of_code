"""
aoc y2023 day 15
https://adventofcode.com/2023/day/15
"""


def d15parse(data):
    """
    parse
    """
    line = data[0]
    steps = []
    for step in line.split(','):
        steps.append(step)
    return steps


def holiday_ascii_string_helper(step):
    """
    get the HASH algorithm value for a given step
    """
    current = 0
    for char in step:
        current += ord(char)
        current = current * 17
        current = current % 256
    return current


def d15p1(data):
    """
    part 1
    """
    result = 0
    for step in data:
        res = holiday_ascii_string_helper(step)
        result += res
    return result


def holiday_ascii_string_helper_arrangement_procedure(boxes, step):
    """
    Modify the box in boxes according to the current step
    """
    action = '=' if '=' in step else '-'
    split_step = step.split(action)
    label = split_step[0]
    box = holiday_ascii_string_helper(label)

    if action == '-':
        try:
            boxes[box].pop(label)
        except KeyError:
            pass
        else:
            if boxes[box] == {}:
                boxes.pop(box)
    else:
        focal_length = int(split_step[1])
        try:
            boxes[box][label] = focal_length
        except KeyError:
            boxes[box] = {label: focal_length}


def d15p2(data):
    """
    part 2
    """
    boxes = {}
    for step in data:
        holiday_ascii_string_helper_arrangement_procedure(boxes, step)

    result = 0
    for box, lenses in boxes.items():
        box_number = box + 1
        lens_number = 0
        focusing_power = 0
        for lens in lenses.values():
            lens_number += 1
            focusing_power += box_number * lens_number * lens
        result += focusing_power

    return result
