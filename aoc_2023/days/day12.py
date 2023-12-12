"""
aoc 2023 day 12
https://adventofcode.com/2023/day/12
"""
from copy import copy
from functools import cache


records = []
with open('data/day12_data.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        split_line = line.split()
        springs = split_line[0]
        groups = [int(x) for x in split_line[1].split(',')]
        records.append((springs, groups))


def count_possibilities(springs, groups):
    """
    count the numer of correct puzzles where
    replacing ? by either . or # would give the correct number of groups
    """
    def valid_group(current, length):
        """
        Check whether the substring starting at current and ending at current + length
        is a group composed by #s and ?s
        """
        return '.' not in springs[current:current + length] \
            and current + length <= len(springs) \
            and (current + length == len(springs) or springs[current + length] in ['.', '?'])

    @cache
    def internal(current, current_group):
        """
        cached recursive exploration of the string to go faster
        """
        if current_group == len(groups):
            return int('#' not in springs[current:])

        if current >= len(springs):
            return 0

        spring = springs[current]
        group = groups[current_group]
        if spring == '#':
            if valid_group(current, group):
                return internal(current + group + 1, current_group + 1)
            else:
                return 0

        elif spring == '?':
            if valid_group(current, group):
                return internal(current + group + 1, current_group + 1) + internal(current + 1, current_group)

        return internal(current+1, current_group)
    return internal(0, 0)


def d12p1():
    """
    You finally reach the hot springs! You can see steam rising from secluded areas attached to the primary, ornate building.
    As you turn to enter, the researcher stops you. "Wait - I thought you were looking for the hot springs, weren't you?" You indicate that this definitely looks like hot springs to you.
    "Oh, sorry, common mistake! This is actually the onsen! The hot springs are next door."
    You look in the direction the researcher is pointing and suddenly notice the massive metal helixes towering overhead. "This way!"
    It only takes you a few more steps to reach the main gate of the massive fenced-off area containing the springs. You go through the gate and into a small administrative building.
    "Hello! What brings you to the hot springs today? Sorry they're not very hot right now; we're having a lava shortage at the moment." You ask about the missing machine parts for Desert Island.
    "Oh, all of Gear Island is currently offline! Nothing is being manufactured at the moment, not until we get more lava to heat our forges. And our springs. The springs aren't very springy unless they're hot!"
    "Say, could you go up and see why the lava stopped flowing? The springs are too cold for normal operation, but we should be able to find one springy enough to launch you up there!"
    There's just one problem - many of the springs have fallen into disrepair, so they're not actually sure which springs would even be safe to use! Worse yet, their condition records of which springs are damaged (your puzzle input) are also damaged! You'll need to help them repair the damaged records.
    In the giant field just outside, the springs are arranged into rows. For each row, the condition records show every spring and whether it is operational (.) or damaged (#). This is the part of the condition records that is itself damaged; for some springs, it is simply unknown (?) whether the spring is operational or damaged.
    However, the engineer that produced the condition records also duplicated some of this information in a different format! After the list of springs for a given row, the size of each contiguous group of damaged springs is listed in the order those groups appear in the row. This list always accounts for every damaged spring, and each number is the entire size of its contiguous group (that is, groups are always separated by at least one operational spring: #### would always be 4, never 2,2).
    So, condition records with no unknown spring conditions might look like this:

    #.#.### 1,1,3
    .#...#....###. 1,1,3
    .#.###.#.###### 1,3,1,6
    ####.#...#... 4,1,1
    #....######..#####. 1,6,5
    .###.##....# 3,2,1

    However, the condition records are partially damaged; some of the springs' conditions are actually unknown (?). For example:

    ???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1

    Equipped with this information, it is your job to figure out how many different arrangements of operational and broken springs fit the given criteria in each row.
    In the first line (???.### 1,1,3), there is exactly one way separate groups of one, one, and three broken springs (in that order) can appear in that row: the first three unknown springs must be broken, then operational, then broken (#.#), making the whole row #.#.###.
    The second line is more interesting: .??..??...?##. 1,1,3 could be a total of four different arrangements. The last ? must always be broken (to satisfy the final contiguous group of three broken springs), and each ?? must hide exactly one of the two broken springs. (Neither ?? could be both broken springs or they would form a single contiguous group of two; if that were true, the numbers afterward would have been 2,3 instead.) Since each ?? can either be #. or .#, there are four possible arrangements of springs.
    The last line is actually consistent with ten different arrangements! Because the first number is 3, the first and second ? must both be . (if either were #, the first number would have to be 4 or higher). However, the remaining run of unknown spring conditions have many different ways they could hold groups of two and one broken springs:

    ?###???????? 3,2,1
    .###.##.#...
    .###.##..#..
    .###.##...#.
    .###.##....#
    .###..##.#..
    .###..##..#.
    .###..##...#
    .###...##.#.
    .###...##..#
    .###....##.#

    In this example, the number of possible arrangements for each row is:

        ???.### 1,1,3 - 1 arrangement
        .??..??...?##. 1,1,3 - 4 arrangements
        ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
        ????.#...#... 4,1,1 - 1 arrangement
        ????.######..#####. 1,6,5 - 4 arrangements
        ?###???????? 3,2,1 - 10 arrangements

    Adding all of the possible arrangement counts together produces a total of 21 arrangements.
    For each row, count all of the different arrangements of operational and broken springs that meet the given criteria. What is the sum of those counts?
    """
    result = 0
    for springs, groups in records:
        result += count_possibilities(springs, groups)
    return result


def d12p2():
    """
    As you look out at the field of springs, you feel like there are way more springs than the condition records list. When you examine the records, you discover that they were actually folded up this whole time!
    To unfold the records, on each row, replace the list of spring conditions with five copies of itself (separated by ?) and replace the list of contiguous groups of damaged springs with five copies of itself (separated by ,).

    So, this row:

    .# 1

    Would become:

    .#?.#?.#?.#?.# 1,1,1,1,1

    The first line of the above example would become:

    ???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3

    In the above example, after unfolding, the number of possible arrangements for some rows is now much larger:

        ???.### 1,1,3 - 1 arrangement
        .??..??...?##. 1,1,3 - 16384 arrangements
        ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
        ????.#...#... 4,1,1 - 16 arrangements
        ????.######..#####. 1,6,5 - 2500 arrangements
        ?###???????? 3,2,1 - 506250 arrangements

    After unfolding, adding all of the possible arrangement counts together produces 525152.
    Unfold your condition records; what is the new sum of possible arrangement counts?
    """
    result = 0
    for springs, groups in records:
        # unfold the values
        springs = '?'.join(springs for i in range(5))
        g = copy(groups)
        groups = []
        for i in range(5):
            groups += g

        # get the result
        result += count_possibilities(springs, groups)

    return result