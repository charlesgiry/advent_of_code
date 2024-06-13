"""
aoc y2023 day 14
https://adventofcode.com/2023/day/14
"""


def move_stone_y_axis(array: list[str], up: bool):
    """
    Move all the stones either up or down
    """
    len_y = len(array)
    len_x = len(array[0])

    steps = [[] for _ in range(len_x)]
    for x in range(len_x):
        step = {'O': 0, '.': 0, '#': 0}
        for y in range(len_y):
            if array[y][x] != '#':
                step[array[y][x]] += 1
            else:
                step['#'] = 1
                steps[x].append(step)
                step = {'O': 0, '.': 0, '#': 0}

        if step['O'] != 0 or step['.'] != 0:
            steps[x].append(step)

    new_array = ['' for _ in range(len_y)]
    for x in range(len_x):
        # get the characters to write
        write = ''
        for step in steps[x]:
            if up:
                write += 'O' * step['O'] + '.' * step['.'] + '#' * step['#']
            else:
                write += '.' * step['.'] + 'O' * step['O'] + '#' * step['#']
        for y in range(len_y):
            new_array[y] += write[y]

    return new_array


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

def d14p1(data):
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
    l = move_stone_y_axis(data, up=True)
    return count_weight(l)


def move_stone_x_axis(array: list[str], right: bool):
    """
    Move all the stones either left or right
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
                if right:
                    new_array[i] = new_array[i] + '.' * dot_count + 'O' * o_count + '#'
                else:
                    new_array[i] = new_array[i] + 'O' * o_count + '.' * dot_count + '#'

                o_count = 0
                previous_sharp = x + 1

        rest = len_x - len(new_array[i])
        dot_count = rest - o_count
        if right:
            new_array[i] = new_array[i] + '.' * dot_count + 'O' * o_count
        else:
            new_array[i] = new_array[i] + 'O' * o_count + '.' * dot_count
    return new_array


def run_cycle(array: list[str]) -> list[str]:
    """
    run all the required functions for a single sc=cycle
    """
    l = move_stone_y_axis(array, up=True)
    l = move_stone_x_axis(l, right=False)
    l = move_stone_y_axis(l, up=False)
    l = move_stone_x_axis(l, right=True)
    return l


def d14p2(data):
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
    l = data
    results = []
    result_encountered = {}

    for i in range(1000000000):
        l = run_cycle(l)
        res = count_weight(l)

        # stock the latest result in the results list
        results.append(res)

        # stock where the result was encountered in the cycles dict
        if res in result_encountered:
            result_encountered[res].append(i)
        else:
            result_encountered[res] = [i]

        # 3 is an arbitrary number at which you'd want to see the pattern start appearing
        # if result is incorrect, you probably need to increase this number
        if len(result_encountered[res]) > 3:
            cycle_len = i - result_encountered[res][-2]
            if cycle_len == 1:
                cycle_len = i - result_encountered[res][-3]

            # check that the pattern fully repeats
            res_found = True
            for j in range(cycle_len):
                if results[i -j] != results[i - cycle_len - j]:
                    res_found = False
                    break

            if res_found:
                cycle = results[-cycle_len:]
                n = (1000000000 - i - 2) % cycle_len
                return cycle[n]

    return count_weight(l)
