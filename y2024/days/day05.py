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
            is_updated = int(splt[1])
            needs_update = int(splt[0])
            if is_updated not in rules:
                rules[is_updated] = []

            rules[is_updated].append(needs_update)

        else:
            splt = line.split(',')
            updates.append([int(i) for i in splt])

    return {
        'rules': rules,
        'updates': updates
    }


def d5p1(data):
    """
    part 1
    """
    print(data)


def d5p2(data):
    """
    part 2
    """
    pass
