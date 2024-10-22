#!/usr/bin/python3
"""

"""
from argparse import ArgumentParser, Namespace
from datetime import datetime, timezone
from importlib import import_module
from pathlib import Path

from utils import measure, fopen, logger, timing


def main(args: Namespace):
    """

    """
    for year in args.year:
        module_name = f'y{year}'
        if Path.is_dir(Path(module_name)):
            module = import_module(f'{module_name}')

            with timing(module_name):
                for day in args.day:
                    day_data = str(day) if day >= 10 else f'0{day}'
                    if Path.is_file(Path(module_name, 'days', f'day{day_data}.py')):
                        with timing(f'{module_name} day {day_data}'):
                            data_folder = Path(f'y{year}', 'data')
                            data_file = Path(data_folder, f'day{day_data}.txt')
                            data = measure(fopen, data_file, show_args=True, show_result=False)

                            if hasattr(module, f'd{day}parse'):
                                func = getattr(module, f'd{day}parse')
                                data = measure(func, data, show_args=False, show_result=False)

                            for part in args.part:
                                func_name = f'd{day}p{part}'
                                func = getattr(module, func_name)
                                measure(func, data, show_args=False, show_result=True)

                                if args.old:
                                    if hasattr(module, f'{func_name}_old'):
                                        func_name = f'd{day}p{part}_old'
                                        func = getattr(module, func_name)
                                        measure(func, data, show_args=False, show_result=True)

                        logger.info('')
            logger.info('')


if __name__ == '__main__':
    parser = ArgumentParser()

    now = datetime.now(timezone.utc)
    max_year = now.year + 1 if now.month == 12 else now.year
    parser.add_argument(
        '-y', '--year',
        help='Execute only a given year',
        action='store',
        nargs='*',
        choices=range(2015, max_year),
        type=int,
        dest='year'
    )

    parser.add_argument(
        '-d', '--day',
        help='Execute only a given day of a year. Depends on --year arg',
        action='store',
        nargs='*',
        choices=range(1, 26),
        type=int,
        dest='day'
    )

    parser.add_argument(
        '-p', '--part',
        help='Execute only a given part for a day. Depends on --day arg',
        action='store',
        nargs='*',
        choices=[1, 2],
        type=int,
        dest='part'
    )

    parser.add_argument(
        '-o', '--old',
        help='Execute "old" methods as well',
        action='store_true',
        dest='old'
    )

    args = parser.parse_args()

    if args.year is None:
        args.year = range(2015, max_year)

    if args.day is None:
        args.day = range(1, 26)

    if args.part is None:
        args.part = [1, 2]

    measure(main, args, show_args=False, show_result=False)
