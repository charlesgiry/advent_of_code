"""
aoc 2023 day 14
https://adventofcode.com/2023/day/14
"""
from copy import copy

with open('data/day14_data.txt', 'r') as file:
    # lines = file.read().splitlines()
    lines = [list(line) for line in file.read().splitlines()]


def move_stone_right(array):
    """
    currently unused, trying to refactor the move stone method to make it more performant
    """
    len_y = len(array)
    len_x = len(array[0])

    signs = [[] for _ in range(len_y)]

    for y in range(len_y):
        for x in range(len_x):
            if array[y][x] == 'O':
                signs[y].append(('O', x))
            if array[y][x] == '#':
                signs[y].append(('#', x))

    new_array = [
        '' for i in range(len_y)
    ]

    for i in range(len_y):
        o_count = 0
        previous_sharp = 0
        for type, x in signs[i]:
            if type == 'O':
                o_count += 1

            if type == '#':
                dot_count = x - previous_sharp - o_count
                new_array[i] = new_array[i] + '.' * dot_count + 'O' * o_count + '#'
                o_count = 0
                previous_sharp = x + 1


        rest = len_x - len(new_array[i])
        dot_count = rest - o_count
        new_array[i] = new_array[i] + '.' * dot_count + 'O' * o_count

    return new_array


# previous badly optimized function to move the stones
def move_stone(array, y, x, mov_y, mov_x):
    """
    move all the "O" stones within the array in the mov_y or mov_x direction
    """
    while True:
        new_y = y + mov_y
        new_x = x + mov_x

        if new_y < 0 \
                or new_y >= len(array) \
                or new_x < 0 \
                or new_x >= len(array[0]) \
                or array[new_y][new_x] == '#':
            break

        array[new_y][new_x], array[y][x] = array[y][x], array[new_y][new_x]
        y, x = new_y, new_x

        if array[y][x] != 'O':
            break


def tilt_up(array):
    """
    move all the stones to the north
    """
    for x in range(len(array[0])):
        for y in range(len(array)):
            if array[y][x] == 'O':
                move_stone(array, y, x, -1, 0)


def count_weight(array):
    """
    count the result from the array
    """
    result = 0
    for y in range(len(array)):
        for x in range(len(array[0])):
            if array[y][x] == 'O':
                result += (len(array) - y)
    return result


def d14p1():
    """
    You reach the place where all of the mirrors were pointing: a massive parabolic reflector dish attached to the side of another large mountain.
    The dish is made up of many small mirrors, but while the mirrors themselves are roughly in the shape of a parabolic reflector dish, each individual mirror seems to be pointing in slightly the wrong direction. If the dish is meant to focus light, all it's doing right now is sending it in a vague direction.
    This system must be what provides the energy for the lava! If you focus the reflector dish, maybe you can go where it's pointing and use the light to fix the lava production.
    Upon closer inspection, the individual mirrors each appear to be connected via an elaborate system of ropes and pulleys to a large metal platform below the dish. The platform is covered in large rocks of various shapes. Depending on their position, the weight of the rocks deforms the platform, and the shape of the platform controls which ropes move and ultimately the focus of the dish.
    In short: if you move the rocks, you can focus the dish. The platform even has a control panel on the side that lets you tilt it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty spaces (.) and rocks (your puzzle input). For example:

    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....

    Start by tilting the lever so all of the rocks will slide north as far as they will go:

    OOOO.#.O..
    OO..#....#
    OO..O##..O
    O..#.OO...
    ........#.
    ..#....#.#
    ..O..#.O.O
    ..O.......
    #....###..
    #....#....

    You notice that the support beams along the north side of the platform are damaged; to ensure the platform doesn't collapse, you should calculate the total load on the north support beams.
    The amount of load caused by a single rounded rock (O) is equal to the number of rows from the rock to the south edge of the platform, including the row the rock is on. (Cube-shaped rocks (#) don't contribute to load.) So, the amount of load caused by each rock in each row is as follows:

    OOOO.#.O.. 10
    OO..#....#  9
    OO..O##..O  8
    O..#.OO...  7
    ........#.  6
    ..#....#.#  5
    ..O..#.O.O  4
    ..O.......  3
    #....###..  2
    #....#....  1

    The total load is the sum of the load caused by all of the rounded rocks. In this example, the total load is 136.
    Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?
    """
    l = copy(lines)
    tilt_up(l)
    return count_weight(l)


def tilt_left(array):
    """
    ove all the stones to the west

    """
    for y in range(len(array)):
        for x in range(len(array[0])):
            if array[y][x] == 'O':
                move_stone(array, y, x, 0, -1)


def tilt_down(array):
    """
    move all the stones to the south
    """
    for x in range(len(array[0])):
        for y in range(len(array) - 1, -1, -1):
            if array[y][x] == 'O':
                move_stone(array, y, x, 1, 0)


def tilt_right(array):
    """
    move all the stones to the east
    """
    for y in range(len(array)):
        for x in range(len(array[0]) - 1, -1, -1):
            if array[y][x] == 'O':
                move_stone(array, y, x, 0, 1)


def run_cycle(array):
    """
    run all the required functions for a single sc=cycle
    """
    tilt_up(array)
    tilt_left(array)
    tilt_down(array)
    tilt_right(array)


def d14p2():
    """
    The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!
    Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.
    Here's what happens in the example above after each of the first few cycles:

    After 1 cycle:
    .....#....
    ....#...O#
    ...OO##...
    .OO#......
    .....OOO#.
    .O#...O#.#
    ....O#....
    ......OOOO
    #...O###..
    #..OO#....

    After 2 cycles:
    .....#....
    ....#...O#
    .....##...
    ..O#......
    .....OOO#.
    .O#...O#.#
    ....O#...O
    .......OOO
    #..OO###..
    #.OOO#...O

    After 3 cycles:
    .....#....
    ....#...O#
    .....##...
    ..O#......
    .....OOO#.
    .O#...O#.#
    ....O#...O
    .......OOO
    #...O###.O
    #.OOO#...O

    This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.
    In the above example, after 1000000000 cycles, the total load on the north support beams is 64.
    Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?
    """
    l = copy(lines)
    results = []
    result_encountered = {}

    for i in range(1000000000):
        run_cycle(l)
        res = count_weight(l)

        # stock the latest result in the results list
        results.append(res)

        # stock where the result was encountered in the cycles dict
        if res in result_encountered:
            result_encountered[res].append(i)
        else:
            result_encountered[res] = [i]

        # if we encountered a result enough times, we'll just try to see if there's a cycle between the two
        # results[i-1] would need to be equal to results[i - cycle - 1] etc...
        if len(result_encountered[res]) > 3:  # 3's an arbitrary number that assumes that we'll have reached the cycling results
            cycle_len = i - result_encountered[res][-2] # to fing the eventual cycle len, just calculate the diff between result_encountered[res][-1] and result_encountered[res][-2]

            # check that the pattern fully repeats
            res_found = True
            for j in range(cycle_len):
                if results[i -j] != results[i - cycle_len - j]:
                    res_found = False
                    break

            if res_found:
                cycle = results[-cycle_len:]    # get the last "cycle_len" results
                n = 1000000000 % cycle_len      # because cycle repeats from now on, calculate which of the results within the cycle to return
                return cycle[n]
