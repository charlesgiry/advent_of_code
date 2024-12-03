"""
aoc y2015 day 8
https://adventofcode.com/2015/day/8
"""
from re import compile


def d8p1(data):
    """
    part 1
    """
    total_len = 0
    content_len = 0

    regexp = compile(r'(\\\\|\\"|\\x([0-9a-fA-F]){2})')

    for line in data:
        total_len += len(line) + 1      # +1 for \n
        content_len += len(line) - 1    # -1: +1 for \n, -2 for quotes
        nb_escape = regexp.findall(line)
        for escaped_char, _ in nb_escape:
            if escaped_char.startswith('\\x'):
                content_len -= 3
            else:
                content_len -= 1
    return total_len - content_len


def encode(str):
    """
    return an "encoded" line with replaced characters
    """
    result = ''
    for char in str:
        if char == '"':
            result += '\\"'
        elif char == '\\':
            result += '\\\\'
        else:
            result += char
    return f'"{result}"'


def d8p2(data):
    """
    part 2
    """
    total_len = 0
    encoded_len = 0
    for line in data:
        total_len += len(line) + 1
        encoded_len += len(encode(line)) + 1

    return encoded_len - total_len
