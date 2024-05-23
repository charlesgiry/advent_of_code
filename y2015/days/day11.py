"""

"""
from string import ascii_lowercase

pack = {ord(c): ord(c) - ord('a') for c in ascii_lowercase}
unpack = {ord(c) - ord('a'): ord(c) for c in ascii_lowercase}


def password_to_list(password):
    return [pack[ord(c)] for c in password]


def list_to_password(passwd_list):
    result = ''
    for c in passwd_list:
        c = c + ord('a')
        result += chr(c)
    return result


def d11parse(data):
    return password_to_list(data[0])


def rule1(password):
    for i in range(len(password) - 2):
        if password[i+1] == password[i] + 1 and password[i+2] == password[i] + 2:
            return True
    return False


def rule2(password):
    i = pack[ord('i')] in password
    o = pack[ord('o')] in password
    l = pack[ord('l')] in password
    return not (i or o or l)


def rule3(password):
    counter = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            counter += 1
            i += 1
        i += 1
    return counter >= 2


def valid_password(password):
    return rule1(password) and rule2(password) and rule3(password)


def increment_password(password):
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
    Santa's previous password expired, and he needs help choosing a new one.
    To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one.
    Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons),
    so he finds his new password by incrementing his old password string repeatedly until it is valid.
    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on.
    Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

    Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:
        Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
        Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
        Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

    For example:
        hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
        abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
        abbcegjk fails the third requirement, because it only has one double letter (bb).
        The next password after abcdefgh is abcdffaa.
        The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
    Given Santa's current password (your puzzle input), what should his next password be?
    """
    current = data
    while not valid_password(current):
        current = increment_password(current)

    return list_to_password(current)


def d11p2(data):
    current = d11p1(data)
    current = password_to_list(current)
    current = increment_password(current)
    return d11p1(current)

