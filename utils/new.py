"""

"""
from datetime import datetime, timezone
from pathlib import Path
import re

FILE_SKELETON = '''"""
TOP_COMMENT
"""


def dXparse(data):
    """
    PARSE_COMMENT
    """
    return data

def dXp1(data):
    """
    P1_COMMENT
    """
    pass

def dXp2(data):
    """
    P2_COMMENT
    """
    pass
'''


def new():
    """
    Create a new file set up to work with the project skeleton, to be faster for a new aoc day
    """
    now = datetime.now(timezone.utc)

    # get year
    y = input('Please enter a year. If left empty, current year will be used\n')
    if y == '':
        y = now.year
    else:
        try:
            y = int(y)
        except ValueError:
            print('Error, y should be a number')
            exit(44)

    # create yYYYY folder and __init__.py
    y_current = Path(f'y{y}')
    try:
        y_current.mkdir()
    except FileExistsError:
        pass
    else:
        with open(y_current / '__init__.py', 'w') as file:
            file.write('"""\n')
            file.write(f'y{y} code\n')
            file.write('"""\n')
            file.write('from .days import *\n')

    # create data folder and __init__.py
    data = y_current / 'data'
    try:
        data.mkdir()
    except FileExistsError:
        pass
    else:
        with open(data / '__init__.py', 'w') as file:
            file.write('"""\n')
            file.write(f'y{y} data\n')
            file.write('"""\n')

    # create days folder and __init__.py
    days = y_current / 'days'
    days_init = days / '__init__.py'
    try:
        days.mkdir()
    except FileExistsError:
        pass
    else:
        with open(days_init, 'w') as file:
            file.write('"""\n')
            file.write(f'y{y} code for each day\n')
            file.write('"""\n')

    # Get date
    d = input('Please enter a day. If left empty, current day will be used\n')
    if d == '':
        d = str(now.day)
    try:
        int(d)
    except ValueError:
        print('Error, d should be a number')
        exit(45)
    # d1c for day with 1 character if < 10. d2c for day with 2 characters always
    d1c = d
    d2c = d
    if len(d) == 1:
        d2c = f'0{d}'

    # perpare file
    top_comment = f'aoc y{y} day {d2c}\n'
    top_comment += f'https://adventofcode.com/{y}/day/{d1c}'
    current_file = FILE_SKELETON
    current_file = re.sub('TOP_COMMENT', top_comment, current_file)
    current_file = re.sub('X', d1c, current_file)

    # create file
    file_path = days / f'day{d2c}.py'
    with open(file_path, 'w') as file:
        file.write(current_file)

    # append newly created file to __init__.py
    with open(days_init, 'a') as file:
        file.write(f'from y{y}.days.day{d2c} import d{d1c}p1, d{d1c}p2, d{d1c}parse')

    # create empty data file
    with open(data / f'day{d2c}.txt', "w") as file:
        file.write('\n')
