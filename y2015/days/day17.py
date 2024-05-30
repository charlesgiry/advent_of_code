"""
aoc y2015 day 17
https://adventofcode.com/2015/day/17
"""
from itertools import combinations


def d17parse(data):
    return [int(i) for i in data]


def d17p1(data):
    """
    The elves bought too much eggnog again - 150 liters this time.
    To fit it all into your refrigerator, you'll need to move it into smaller containers.
    You take an inventory of the capacities of the available containers.
    For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.
    If you need to store 25 liters, there are four ways to do it:
        15 and 10
        20 and 5 (the first 5)
        20 and 5 (the second 5)
        15, 5, and 5
    Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
    """
    result = 0
    for i in range(len(data)):
        for containers in combinations(data, i):
            if sum(containers) == 150:
                result += 1
    return result


def d17p2(data):
    """
    While playing with all the containers in the kitchen, another load of eggnog arrives!
    The shipping and receiving department is requesting as many containers as you can spare.
    Find the minimum number of containers that can exactly fit all 150 liters of eggnog.
    How many different ways can you fill that number of containers and still hold exactly 150 litres?

    In the example above, the minimum number of containers was two.
    There were three ways to use that many containers, and so the answer there would be 3.
    """
    lens = dict()
    for i in range(len(data)):
        for containers in combinations(data, i):
            if sum(containers) == 150:
                len_containers = len(containers)
                if len_containers not in lens:
                    lens[len_containers] = []
                lens[len_containers].append(containers)
    return len(lens[min(lens.keys())])
