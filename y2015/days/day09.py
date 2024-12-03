"""
aoc y2015 day 9
https://adventofcode.com/2015/day/9
"""
from itertools import permutations


def d9parse(data):
    """
    parse
    """
    targets = {}
    distances = {}
    towns = set()

    for line in data:
        splt = line.split(' = ')
        distance = int(splt[1])
        travel = splt[0].split(' to ')
        start = travel[0]
        arrival = travel[1]

        if start in targets:
            targets[start].append(arrival)
        else:
            targets[start] = [arrival]

        if arrival in targets:
            targets[arrival].append(start)
        else:
            targets[arrival] = [start]

        distances[(start, arrival)] = distance
        distances[(arrival, start)] = distance
        towns.add(start)
        towns.add(arrival)

        for town in towns:
            if town not in targets:
                targets[town] = []

    return (targets, distances, list(towns))


def get_valid_paths(paths, targets):
    """

    """
    valid_paths = []
    for path in paths:
        for i in range(len(path) - 1):
            start = path[i]
            arrival = path[i+1]

            if arrival not in targets[start]:
                break
        else:
            valid_paths.append(list(path))
    return valid_paths


def get_path_distances(valid_paths, distances):
    """
    calculate path
    """
    paths_len = {}
    for path in valid_paths:
        path_len = 0
        for i in range(len(path) -1):
            start = path[i]
            arrival = path[i + 1]
            path_len += distances[(start, arrival)]
        paths_len[path_len] = path
    return paths_len


def d9p1(data):
    """
    part 1
    """
    targets, distances, towns = data
    paths = permutations(towns, len(towns))
    valid_paths = get_valid_paths(paths, targets)
    path_distances = get_path_distances(valid_paths, distances)

    min_path = min(path_distances.keys())
    return min_path


def d9p2(data):
    """
    part 2
    """
    targets, distances, towns = data
    paths = permutations(towns, len(towns))
    valid_paths = get_valid_paths(paths, targets)
    path_distances = get_path_distances(valid_paths, distances)

    max_path = max(path_distances.keys())
    return max_path
