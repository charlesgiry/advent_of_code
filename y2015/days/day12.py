"""
aoc y2015 day 12
https://adventofcode.com/2015/day/12
"""
from json import loads


def d12parse(data):
    """
    parse
    """
    data = loads(data[0])
    return data


def unpack(data):
    """
    explore recursively a dict and return all the int inside
    """
    if isinstance(data, dict):
        for _, values in data.items():
            yield from unpack(values)
    elif isinstance(data, list):
        for values in data:
            yield from unpack(values)
    elif isinstance(data, int):
        yield data


def d12p1(data):
    """
    part 1
    """
    int_list = unpack(data)
    result = 0
    for i in int_list:
        result += i

    return result


def unpack_ignore_red(data):
    """
    explore recursively a dict and return all the int inside
    ignore all dicts that contain "red" as key or value
    """
    if isinstance(data, dict):
        if any(key == 'red' or value == 'red' for key, value in data.items()):
            return
        for _, values in data.items():
            yield from unpack_ignore_red(values)
    elif isinstance(data, list):
        for values in data:
            yield from unpack_ignore_red(values)
    elif isinstance(data, int):
        yield data


def d12p2(data):
    """
    part 2
    """
    int_list = unpack_ignore_red(data)
    result = 0
    for i in int_list:
        result += i

    return result
