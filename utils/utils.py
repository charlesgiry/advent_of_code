"""

"""
from time import perf_counter
from traceback import print_exc

from utils.log import logger


def measure(func, *args, **kwargs):
    """
    measure the performances of a method execution using time.perf_counter
    """
    start = perf_counter()

    show_args = kwargs.pop('show_args') if 'show_args' in kwargs else True
    show_result = kwargs.pop('show_result') if 'show_result' in kwargs else True

    if show_args:
        print_str = f'{func.__name__}' \
                    f'({", ".join(str(arg) for arg in args)}' \
                    f'{", " if args and kwargs else ""}' \
                    f'{", ".join(f"{key}={value}" for key, value in kwargs.items())})'
    else:
        print_str = f'{func.__name__}'
    try:
        result = func(*args, **kwargs)

    except:
        perf = perf_counter() - start
        perf = "{:.6f}".format(perf)
        print_str = f'{print_str} - encountered an exception after {perf}s'
        logger.info(print_str)
        print_exc()

    else:
        perf = perf_counter() - start
        perf = "{:.6f}".format(perf)
        if result is not None and show_result:
            print_str = f'{print_str} : {result} - took {perf}s'
        else:
            print_str = f'{print_str} - took {perf}s'
        logger.info(print_str)
        return result


def fopen(filepath):
    """

    """
    lines = []
    with open(filepath, 'r') as file:
        for l in file.read().splitlines():
            lines.append(l)
    return lines


class timing:
    """
    Measure the time taken between the start and the end of a code snippet
    use:
    with timing('text to write at the end'):
        code snippet
    """
    start: float
    text: str

    def __init__(self, text: str):
        self.text = text

    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        perf = "{:.6f}".format(perf_counter() - self.start)
        logger.info(f'{self.text} - took {perf}s')
