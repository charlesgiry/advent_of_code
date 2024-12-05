"""
aoc y2024 day 05
https://adventofcode.com/2024/day/5
"""


def d5parse(data):
    """
    parse
    """
    rules = {}
    updates = []
    is_rules = True
    for line in data:
        if line == '':
            is_rules = False
        elif is_rules:
            splt = line.split('|')
            before = int(splt[0])
            after = int(splt[1])
            if after not in rules:
                rules[after] = set()
            rules[after].add(before)
        else:
            splt = line.split(',')
            updates.append([int(i) for i in splt])

    return {
        'rules': rules,
        'updates': updates
    }


# keep incorrect updates from p1 to avoid having to revalidate the entire file
INCORRECT_UPDATES = []


def d5p1(data):
    """
    part 1
    """
    rules = data['rules']
    updates = data['updates']
    result = 0
    for update in updates:
        l = len(update)
        for i in range(l):
            if update[i] in rules and any(val in rules[update[i]] for val in update[i + 1:]):
                INCORRECT_UPDATES.append(update)
                break
        else:
            result += update[l // 2]
    return result


def d5p2(data):
    """
    part 2
    extremely inefficient solution, but will do until i find something better
    """
    result = 0
    rules = data['rules']
    for update in INCORRECT_UPDATES:
        l = len(update)
        i = 0
        while i < l:
            start = i
            cont = True
            while update[start] in rules and any(val in rules[update[start]] for val in update[start+1:]):
                update[start], update[start+1] = update[start+1], update[start]
                start += 1
                cont = False
            if cont:
                i += 1
        result += update[l // 2]
    return result
