"""
aoc y2023 day 9
https://adventofcode.com/2023/day/9
"""


def d9parse(data):
    """
    parse
    """
    lines = []
    for l in data:
        line = []
        for value in l.split():
            line.append(int(value))
        lines.append(line)
    return lines


def extrapolate_value(starting_list, backward):
    """
    extrapolate the value to find on p1 or p2 depending whether it's a backward extrapolation or not
    """
    # build a stack of list until the list is full of zeroes
    stack = []
    # if we have to extrapolate backwards, we can simply invert the input and keep the method as is
    current_list = starting_list[::-1] if backward else starting_list

    while True:
        stack.append(current_list)
        new_list = []
        for i in range(len(current_list)-1):
            new_list.append(current_list[i+1] - current_list[i])

        if set(new_list) == {0}:
            stack.append(new_list)
            break
        current_list = new_list

    # extrapolate the value to find based on previous list and whether it's a backward extrapolation or not
    calculation_value = 0
    while stack:
        current_list = stack.pop()
        last_elem = current_list[-1]
        calculation_value = last_elem + calculation_value

    return calculation_value


def d9p1(data):
    """
    part 1
    """
    result = 0
    for line in data:
        result += extrapolate_value(line, False)
    return result


def d9p2(data):
    """
    part 2
    """
    result = 0
    for line in data:
        result += extrapolate_value(line, True)
    return result
