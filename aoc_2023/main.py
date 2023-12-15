from time import perf_counter
from traceback import print_exc

from days.day01 import d1p1, d1p2
from days.day02 import d2p1, d2p2
from days.day03 import d3p1, d3p2
from days.day04 import d4p1, d4p2
from days.day05 import d5p1, d5p2
from days.day06 import d6p1, d6p2
from days.day07 import d7p1, d7p2
from days.day08 import d8p1, d8p2
from days.day09 import d9p1, d9p2
from days.day10 import d10p1, d10p2
from days.day11 import d11p1, d11p2
from days.day12 import d12p1, d12p2
from days.day13 import d13p1, d13p2
from days.day14 import d14p1, d14p2
from days.day15 import d15p1, d15p2


def measure(func, *args, **kwargs):
    """
    measure the performances of a method execution using time.perf_counter
    """
    start = perf_counter()
    print_str = f'{func.__name__}' \
                f'({", ".join(str(arg) for arg in args)}' \
                f'{", " if args and kwargs else ""}' \
                f'{", ".join(f"{key}={value}" for key, value in kwargs.items())})'
    try:
        result = func(*args, **kwargs)

    except:
        perf = perf_counter() - start
        perf = "{:.6f}".format(perf)
        print_str = f'{print_str} - encountered an exception after {perf}s'
        print_exc()

    else:
        perf = perf_counter() - start
        perf = "{:.6f}".format(perf)
        if result:
            print_str = f'{print_str}: {result} - took {perf}s'
        else:
            print_str = f'{print_str} - took {perf}s'

    print(print_str)


def main():
    """
    main
    """
    print('')
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

    measure(d9p1)
    measure(d9p2)
    print('')

    measure(d10p1)
    measure(d10p2)
    print('')

    measure(d11p1)
    measure(d11p2)
    print('')

    measure(d12p1)
    measure(d12p2)
    print('')

    measure(d13p1)
    measure(d13p2)
    print('')

    measure(d14p1)
    measure(d14p2)
    print('')

    measure(d15p1)
    measure(d15p2)
    print('')


if __name__ == '__main__':
    measure(main)
