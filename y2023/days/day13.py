"""
aoc y2023 day 13
https://adventofcode.com/2023/day/13
"""


def d13parse(data):
    """
    parse
    """
    vertical_puzzles = []
    horizontal_puzzles = []

    vertical_puzzle = ['' for i in range(len(data[0]))]
    horizontal_puzzle = []

    for i in range(len(data)):
        line = data[i]

        if i == len(data) - 1:
            vertical_puzzles.append(vertical_puzzle)
            horizontal_puzzles.append(horizontal_puzzle)

        if line == '':
            vertical_puzzles.append(vertical_puzzle)
            horizontal_puzzles.append(horizontal_puzzle)
            vertical_puzzle = ['' for i in range(len(data[i+1]))]
            horizontal_puzzle = []

        else:
            horizontal_puzzle.append(line)
            for j in range(len(line)):
                vertical_puzzle[j] += line[j]

    return (horizontal_puzzles, vertical_puzzles)

def find_symmetry(puzzle):
    """
    check for (horizontal) symmetry within the puzzle
        note: for vertical symmetry, we just run horizontal symmetry on the vertical puzzle
    """
    for i in range(len(puzzle) - 1):
        if puzzle[i] == puzzle[i+1]:
            l1 = i + 2
            l2 = i - 1
            while 0 <= l2 and l1 < len(puzzle):
                if puzzle[l1] != puzzle[l2]:
                    break
                l1 += 1
                l2 -= 1
            else:
                return i + 1
    return 0


def d13p1(data):
    """
    part 1
    """
    horizontal_puzzles, vertical_puzzles = data
    result = 0

    for i in range(len(horizontal_puzzles)):
        horizontal_puzzle = horizontal_puzzles[i]
        vertical_puzzle = vertical_puzzles[i]

        result += find_symmetry(horizontal_puzzle) * 100
        result += find_symmetry(vertical_puzzle)

    return result


def differences(l1, l2):
    """
    calculate the number of differences between two strings
    """
    result = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            result += 1
    return result


def fix_smudge(puzzle, smudge):
    """
    find the line where there's a smudge of a given size
    """
    assert smudge >= 1

    for i in range(len(puzzle) - 1):
        smudge_repaired = False
        diff = differences(puzzle[i], puzzle[i + 1])

        if diff <= smudge:
            if diff == smudge:
                smudge_repaired = True
            l1 = i + 2
            l2 = i - 1
            while 0 <= l2 and l1 < len(puzzle):
                diff = differences(puzzle[l1], puzzle[l2])
                if diff > smudge:
                    break
                elif diff == smudge and smudge_repaired:
                    break
                elif diff == smudge:
                    smudge_repaired = True
                l1 += 1
                l2 -= 1
            else:
                if smudge_repaired:
                    return i + 1
    return 0


def d13p2(data):
    """
    part 2
    """
    horizontal_puzzles, vertical_puzzles = data
    result = 0
    for i in range(len(horizontal_puzzles)):
        horizontal_puzzle = horizontal_puzzles[i]
        vertical_puzzle = vertical_puzzles[i]

        result += fix_smudge(horizontal_puzzle, 1) * 100
        result += fix_smudge(vertical_puzzle, 1)

    return result
