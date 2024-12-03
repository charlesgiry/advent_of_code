"""
aoc y2023 day 6
https://adventofcode.com/2023/day/6
"""
from functools import reduce
from math import sqrt, ceil


def d6parse(data: list[str]):
    """
    parse
    """
    times = data[0].split(':')[1].split()
    distances = data[1].split(':')[1].split()

    # get all the races for p1
    races = []
    for i in range(len(times)):
        race = {
            'time': int(times[i]),
            'distance': int(distances[i])
        }
        races.append(race)

    # generate the big race for p2
    big_race = {
        'time': int(''.join(t for t in times)),
        'distance': int(''.join(d for d in distances))
    }

    return {
        'races': races,
        'big_race': big_race
    }


def d6p1(data):
    """
    part 1
    """
    results = []
    races = data['races']
    for race in races:
        # print(f'race {race}')
        ways_to_win = 0
        for i in range(race['time']):
            speed = i
            movement_time = race['time'] - i
            distance_moved = speed * movement_time
            # print(f'you press the button for {i}ms, the boat moves for {movement_time}ms at {speed}mm/ms. It ran for {distance_moved}mm')

            if distance_moved > race['distance']:
                # print('  that\'s a win!')
                ways_to_win += 1

        # print(f'there are {ways_to_win} ways to win this race')
        results.append(ways_to_win)

    # multiply the results together
    result = reduce(lambda x, y: x * y, results)
    return result


def d6p2(data):
    """
    part 2
    """
    big_race = data['big_race']

    # solve with quadratic equations
    time = big_race['time']
    distance = big_race['distance']

    quadratic_sqrt = sqrt(pow(time, 2) - (4 * (distance + 1)))
    lower_bound = ceil((time - quadratic_sqrt) / 2)
    upper_bound = ceil((time + quadratic_sqrt) / 2)

    result = upper_bound - lower_bound

    return result


def d6p2_old(data):
    """
    first attempt as bruteforcing the solution is very fast for this day
    """
    big_race = data['big_race']
    for i in range(big_race['time']):
        speed = i
        movement_time = big_race['time'] - i
        distance_moved = speed * movement_time

        if distance_moved > big_race['distance']:
            min_winning = i
            max_winning = big_race['time'] - min_winning
            result = max_winning - min_winning + 1  # +1 as i's first value is 0

            return result

    return None
