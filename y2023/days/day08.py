"""
aoc y2023 day 8
https://adventofcode.com/2023/day/8
"""
import functools
from math import lcm


def d8parse(data):
    """
    parse
    """
    directions = data[0]
    map = {}
    for line in data[2:]:
        location = {
            'L': line[7:10],
            'R': line[12:15]
        }
        loc_code = line[0:3]
        map[loc_code] = location

    return {
        'directions': directions,
        'map': map
    }


def compute_new_location(location, move, map):
    """
    get a new location from a location and a move
    """
    return map[location][move]


def get_move(direction):
    """
    get the current move and update the direction
    cache the result since it'll loop
    """
    return direction[0], direction[1:]


def d8p1(data):
    """
    part 1
    """
    directions = data['directions']
    map = data['map']
    result = 0
    current_direction = directions
    current_location = 'AAA'

    while current_location != 'ZZZ':
        if len(current_direction) == 0:
            current_direction = directions
        current_move, current_direction = get_move(current_direction)
        current_location = compute_new_location(current_location, current_move, map)
        result += 1

    return result


def find_way(starting_location, directions, map):
    """
    get the number of steps to reach a location that ends with Z from a starting location
    """
    result = 0
    current_direction = directions
    current_location = starting_location

    while current_location[-1] != 'Z':
        if len(current_direction) == 0:
            current_direction = directions
        current_move, current_direction = get_move(current_direction)
        current_location = compute_new_location(current_location, current_move, map)
        result += 1

    return result


def d8p2(data):
    """
    part 2
    """
    map = data['map']
    directions = data['directions']
    current_locations = []
    for location in map.keys():
        if location[-1] == 'A':
            current_locations.append(location)

    # find the required number of steps
    steps_for_result = [find_way(x, directions, map) for x in current_locations]

    # find the lower common denominator for these results
    result = lcm(*steps_for_result)

    return result
