"""
aoc y2015 day 19
https://adventofcode.com/2015/day/19
"""
from functools import cache
from random import shuffle

token_list = set()


def d19parse(data):
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
    results = []
    for token in token_list:
        if token.startswith(c):
            results.append(token)
    return results


def d19p1(data):
    """
    Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.
    Red-Nosed Reindeer biology isn't similar to regular reindeer biology;
    Rudolph is going to need custom-made medicine.
    Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.
    The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant,
    capable of constructing any Red-Nosed Reindeer molecule you need.
    It works by starting with some input molecule and then doing a series of replacements, one per step,
    until it has the right molecule.
    However, the machine has to be calibrated before it can be used.
    Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

    For example, imagine a simpler machine that supports only the following replacements:
        H => HO
        H => OH
        O => HH
    Given the replacements above and starting with HOH, the following molecules could be generated:
        HOOH (via H => HO on the first H).
        HOHO (via H => HO on the second H).
        OHOH (via H => OH on the first H).
        HOOH (via H => OH on the second H).
        HHHH (via O => HH).
    So, in the example above, there are 4 distinct molecules
    (not five, because HOOH appears twice) after one replacement from HOH.
    Santa's favorite molecule, HOHOHO, can become 7 distinct molecules
    (over nine replacements: six from H, and three from O).

    The machine replaces without regard for the surrounding characters.
    For example, given the string H2O, the transition H => OO would result in OO2O.
    Your puzzle input describes all of the possible replacements and,
    at the bottom, the medicine molecule for which you need to calibrate the machine.
    How many distinct molecules can be created after all the different ways you can do one replacement
    on the medicine molecule?
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
    Now that the machine is calibrated, you're ready to begin molecule fabrication.
    Molecule fabrication always begins with just a single electron, e, and applying replacements one at a time,
    just like the ones during calibration.

    For example, suppose you have the following replacements:
        e => H
        e => O
        H => HO
        H => OH
        O => HH
    If you'd like to make HOH, you start with e, and then make the following replacements:

        e => O to get O
        O => HH to get HH
        H => OH (on the second H) to get HOH
    So, you could make HOH after 3 steps.
    Santa's favorite molecule, HOHOHO, can be made in 6 steps.

    How long will it take to make the medicine?
    Given the available replacements and the medicine molecule in your puzzle input,
    what is the fewest number of steps to go from e to the medicine molecule?
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
