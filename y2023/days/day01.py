"""
aoc y2023 day 1
https://adventofcode.com/2023/day/1
"""
from re import compile


def d1p1(data):
    """
    part 1
    """
    # use a regexp to find all the digits
    result = 0
    regexp1 = compile(r'\d')
    for line in data:
        number_in_line = regexp1.findall(line)

        line_number = number_in_line[0] + number_in_line[-1]
        result += int(line_number)
    return result


def d1p2(data):
    """
    part 2
    """
    # use a regexp to find all the digits, as well as digits in str format
    # make sure regexp has positive lookahead for twone => [2, 1] cases
    result = 0
    regexp2 = compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
    for line in data:
        number_in_line = regexp2.findall(line)

        # transform digits in str format into digit format
        for i in range(0, len(number_in_line)):
            if number_in_line[i] == 'one':
                number_in_line[i] = '1'
            elif number_in_line[i] == 'two':
                number_in_line[i] = '2'
            elif number_in_line[i] == 'three':
                number_in_line[i] = '3'
            elif number_in_line[i] == 'four':
                number_in_line[i] = '4'
            elif number_in_line[i] == 'five':
                number_in_line[i] = '5'
            elif number_in_line[i] == 'six':
                number_in_line[i] = '6'
            elif number_in_line[i] == 'seven':
                number_in_line[i] = '7'
            elif number_in_line[i] == 'eight':
                number_in_line[i] = '8'
            elif number_in_line[i] == 'nine':
                number_in_line[i] = '9'

        line_number = number_in_line[0] + number_in_line[-1]
        result += int(line_number)
    return result
