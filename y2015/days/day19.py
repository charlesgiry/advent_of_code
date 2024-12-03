"""
aoc y2015 day 19
https://adventofcode.com/2015/day/19
"""
from functools import cache
from random import shuffle

token_list = set()


def d19parse(data):
    """
    parse
    """
    puzzle = data[-1]
    data = data[:-2]

    tokens = {}
    for line in data:
        token, result = line.split(' => ')
        if token not in tokens:
            tokens[token] = []
        tokens[token].append(result)
        token_list.add(token)

    return puzzle, tokens


@cache
def lookahead(c):
    """

    """
    results = []
    for token in token_list:
        if token.startswith(c):
            results.append(token)
    return results


def d19p1(data):
    """
    part 1
    """
    puzzle, tokens = data
    i = 0
    current = ''
    unique_molecules = set()
    while i < len(puzzle):
        current += puzzle[i]
        while lookahead(current):
            i += 1
            current += puzzle[i]
        else:
            current = current[:-1]
            if current in tokens:
                for replacement in tokens[current]:
                    new_molecule = puzzle[:i-len(current)] + replacement + puzzle[i:]
                    unique_molecules.add(new_molecule)
            current = puzzle[i]
        i += 1

    # last iteration
    if current in tokens:
        for replacement in tokens[current]:
            new_molecule = puzzle[:i - len(current)] + replacement + puzzle[i:]
            unique_molecules.add(new_molecule)

    return len(unique_molecules)


def d19p2(data):
    """
    part 2
    """
    # Mostly borrowed from https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4cu5b/
    puzzle, tokens = data

    revert_token = []
    for pre_trans in tokens:
        for post_trans in tokens[pre_trans]:
            revert_token.append((pre_trans, post_trans))

    result = 0
    target = puzzle
    while target != 'e':
        attempt = target

        for pre_trans, post_trans in revert_token:
            if post_trans not in target:
                continue

            target = target.replace(post_trans, pre_trans, 1)
            result += 1

        if attempt == target:
            result = 0
            target = puzzle
            shuffle(revert_token)

    return result
