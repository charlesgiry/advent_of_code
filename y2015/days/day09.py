"""
aoc y2015 day 9
https://adventofcode.com/2015/day/9
"""
from itertools import permutations


def d9parse(data):
    """

    """
    towns = set()

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
    Every year, Santa manages to deliver all of his presents in a single night.
    This year, however, he has some new locations to visit;
    his elves have provided him the distances between every pair of locations.
    He can start and end at any two (different) locations he wants, but he must visit each location exactly once.
    What is the shortest distance he can travel to achieve this?

    For example, given the following distances:
        London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141

    The possible routes are therefore:
        Dublin -> London -> Belfast = 982
        London -> Dublin -> Belfast = 605
        London -> Belfast -> Dublin = 659
        Dublin -> Belfast -> London = 659
        Belfast -> Dublin -> London = 605
        Belfast -> London -> Dublin = 982
    The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

    What is the distance of the shortest route?
    """
    targets, distances, towns = data
    paths = permutations(towns, len(towns))
    valid_paths = get_valid_paths(paths, targets)
    path_distances = get_path_distances(valid_paths, distances)

    min_path = min(path_distances.keys())
    return min_path


def d9p2(data):
    """
    The next year, just to show off, Santa decides to take the route with the longest distance instead.
    He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.
    For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
    What is the distance of the longest route?
    """
    targets, distances, towns = data
    paths = permutations(towns, len(towns))
    valid_paths = get_valid_paths(paths, targets)
    path_distances = get_path_distances(valid_paths, distances)

    max_path = max(path_distances.keys())
    return max_path
