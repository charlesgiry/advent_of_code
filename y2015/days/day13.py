"""
aoc y2015 day 13
https://adventofcode.com/2015/day/13
"""
from itertools import permutations


def d13parse(data):
    """
    parse
    """
    persons = set()
    p1_p2 = {}
    for line in data:
        line_split = line.split('would')
        happiness_split = line_split[1].split()
        person1 = line_split[0].rstrip()
        person2 = happiness_split[-1][:-1]
        happiness = int(happiness_split[1])
        if happiness_split[0] == 'lose':
            happiness *= -1

        if person1 not in p1_p2:
            p1_p2[person1] = {}
        p1_p2[person1][person2] = happiness
        persons.add(person1)
        persons.add(person2)

    return p1_p2, persons


def calc_happiness(p1_p2, person, left, right):
    """

    """
    happiness = 0
    happiness += p1_p2[person][left]
    happiness += p1_p2[person][right]
    return happiness


def find_best_table(p1_p2, persons):
    """

    """
    combs = permutations(persons, len(persons))
    best_happiness = 0
    for table in combs:
        happiness = 0
        for i in range(len(table)):
            person = table[i]
            previous_person = table[i - 1] if i > 0 else table[-1]
            next_person = table[i + 1] if i < len(table) - 1 else table[0]
            happiness += calc_happiness(p1_p2, person, previous_person, next_person)

        if happiness >= best_happiness:
            best_happiness = happiness

    return best_happiness


def d13p1(data):
    """
    part 1
    """
    p1_p2, persons = data
    return find_best_table(p1_p2, persons)


def d13p2(data):
    """
    part 2
    """
    p1_p2, persons = data
    me = 'Me'
    persons.add(me)
    p1_p2[me] = {}

    for person in persons:
        p1_p2[me][person] = 0
        p1_p2[person][me] = 0

    return find_best_table(p1_p2, persons)
