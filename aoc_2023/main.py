from time import perf_counter

from days.day01 import d1p1, d1p2
from days.day02 import d2p1, d2p2
from days.day03 import d3p1, d3p2
from days.day04 import d4p1, d4p2
from days.day05 import d5p1, d5p2
from days.day06 import d6p1, d6p2
from days.day07 import d7p1, d7p2
from days.day08 import d8p1, d8p2


def measure(func):
    start = perf_counter()
    result = func()
    perf = perf_counter() - start
    perf = "{:.4f}".format(perf)
    print(f'{func.__name__}: {result} - took {perf}s')


if __name__ == '__main__':
    measure(d1p1)
    measure(d1p2)
    print('')

    measure(d2p1)
    measure(d2p2)
    print('')

    measure(d3p1)
    measure(d3p2)
    print('')

    measure(d4p1)
    measure(d4p2)
    print('')

    measure(d5p1)
    measure(d5p2)
    print('')

    measure(d6p1)
    measure(d6p2)
    print('')

    measure(d7p1)
    measure(d7p2)
    print('')


    measure(d8p1)
    measure(d8p2)
    print('')
