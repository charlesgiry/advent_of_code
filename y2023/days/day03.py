"""
aoc y2023 day 3
https://adventofcode.com/2023/day/3
"""


def d3parse(data):
    numbers = []
    symbols = []

    y = 0
    len_x = len(data) - 1
    len_y = len(data[0]) - 1

    for line in data:
        x = 0
        while x < len(line):
            if line[x].isdigit():
                number = {
                    'min_x': x,
                    'max_x': x,
                    'y': y,
                    'number': line[x]
                }
                x += 1
                while x < len(line) and line[x].isdigit():
                    number['max_x'] = x
                    number['number'] += line[x]
                    x += 1

                number['number'] = int(number['number'])
                numbers.append(number)

            if x < len(line) and line[x] != '.' and not line[x].isdigit():
                symbol = {
                    'x': x,
                    'y': y,
                    'symbol': line[x]
                }
                symbols.append(symbol)

            x += 1
        y += 1

    return {
        'numbers': numbers,
        'symbols': symbols,
        'len_x': len_x,
        'len_y': len_y
    }


def d3p1(data):
    """
    You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.
    It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
    "Aaah!"
    You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
    The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
    The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
    Here is an example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
    Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
    """
    result = 0
    len_x = data['len_x']
    len_y = data['len_y']

    # for each symbol, find all the related numbers
    for symbol in data['symbols']:
        for number in data['numbers']:
            min_x = number['min_x'] -1 if number['min_x'] -1 >= 0 else 0
            min_y = number['y'] - 1 if number['y'] -1 >= 0 else 0
            max_x = number['max_x'] + 1 if number['max_x'] + 1 <= len_x else len_x
            max_y = number['y'] + 1 if number['y'] + 1 <= len_y else len_y

            if min_x <= symbol['x'] <= max_x and min_y <= symbol['y'] <= max_y:
                result += number['number']

            if number['y'] >= symbol['y'] + 2:
                break
                # if cursor is 2 lines after a symbol, we can stop since we know it can't be in contact

    return result


def d3p2(data):
    """
    The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.
    You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.
    Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.
    The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.
    This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

    Consider the same engine schematic again:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.
    """
    result = 0
    len_x = data['len_x']
    len_y = data['len_y']
    # for each "*" symbol, find all the related numbers
    for symbol in data['symbols']:
        if symbol['symbol'] == '*':
            related_numbers = []

            for number in data['numbers']:
                min_x = number['min_x'] - 1 if number['min_x'] - 1 >= 0 else 0
                min_y = number['y'] - 1 if number['y'] - 1 >= 0 else 0
                max_x = number['max_x'] + 1 if number['max_x'] + 1 <= len_x else len_x
                max_y = number['y'] + 1 if number['y'] + 1 <= len_y else len_y

                if min_x <= symbol['x'] <= max_x and min_y <= symbol['y'] <= max_y:
                    related_numbers.append(number)

                if number['y'] >= symbol['y'] + 2:
                    break
                    # if there is more than 2 numbers in contact, we can stop the loop, it's not a gear

            if len(related_numbers) == 2:
                gear_ratio = related_numbers[0]['number'] * related_numbers[1]['number']
                result += gear_ratio

    return result
