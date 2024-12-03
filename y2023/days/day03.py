"""
aoc y2023 day 3
https://adventofcode.com/2023/day/3
"""


def d3parse(data):
    """
    parse
    """
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
    part 1
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
    part 2
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
