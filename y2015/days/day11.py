"""
aoc y2015 day 11
https://adventofcode.com/2015/day/11
"""
from string import ascii_lowercase

pack = {ord(c): ord(c) - ord('a') for c in ascii_lowercase}
unpack = {ord(c) - ord('a'): ord(c) for c in ascii_lowercase}


def password_to_list(password):
    """

    """
    return [pack[ord(c)] for c in password]


def list_to_password(passwd_list):
    """

    """
    result = ''
    for c in passwd_list:
        c = c + ord('a')
        result += chr(c)
    return result


def d11parse(data):
    """
    parse
    """
    return password_to_list(data[0])


def rule1(password):
    """

    """
    for i in range(len(password) - 2):
        if password[i+1] == password[i] + 1 and password[i+2] == password[i] + 2:
            return True
    return False


def rule2(password):
    """

    """
    i = pack[ord('i')] in password
    o = pack[ord('o')] in password
    l = pack[ord('l')] in password
    return not (i or o or l)


def rule3(password):
    """

    """
    counter = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            counter += 1
            i += 1
        i += 1
    return counter >= 2


def valid_password(password):
    """

    """
    return rule1(password) and rule2(password) and rule3(password)


def increment_password(password):
    """

    """
    current_len = len(password) - 1
    if password[current_len] == pack[ord('z')] + 1:
        current_index = current_len
        while password[current_index] == pack[ord('z')] + 1:
            password[current_index] = pack[ord('a')]
            current_index -= 1
            password[current_index] += 1
            if current_index == -1:
                password.append(pack[ord('a')])
                current_len = len(password) - 1
                current_index = current_len
    else:
        password[current_len] += 1

    return password


def d11p1(data):
    """
    part 1
    """
    current = data
    while not valid_password(current):
        current = increment_password(current)

    return list_to_password(current)


def d11p2(data):
    """
    part 2
    """
    current = d11p1(data)
    current = password_to_list(current)
    current = increment_password(current)
    return d11p1(current)
