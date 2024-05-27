"""
aoc y2015 day 12
https://adventofcode.com/2015/day/12
"""
from json import loads


def d12parse(data):
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
    Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.
    They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

    For example:
        [1,2,3] and {"a":2,"b":4} both have a sum of 6.
        [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
        {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
        [] and {} both have a sum of 0.

    You will not encounter any strings containing numbers.
    What is the sum of all numbers in the document?
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
    Uh oh - the Accounting-Elves have realized that they double-counted everything red.
    Ignore any object (and all of its children) which has any property with the value "red".
    Do this only for objects ({...}), not arrays ([...]).

        [1,2,3] still has a sum of 6.
        [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
        {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
        [1,"red",5] has a sum of 6, because "red" in an array has no effect.
    """
    int_list = unpack_ignore_red(data)
    result = 0
    for i in int_list:
        result += i

    return result
