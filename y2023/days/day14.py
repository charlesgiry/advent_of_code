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
    part 1
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
    part 2
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
