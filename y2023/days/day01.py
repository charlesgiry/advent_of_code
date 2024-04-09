"""
aoc y2023 day 1
https://adventofcode.com/2023/day/1
"""
from re import compile


def d1p1(data):
    """
    Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.
    You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.
    Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
    You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").
    As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
    The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
    Consider your entire calibration document. What is the sum of all of the calibration values?
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
    Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
    Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
    What is the sum of all of the calibration values?
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
