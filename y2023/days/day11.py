"""
aoc y2023 day 11
https://adventofcode.com/2023/day/11
"""
from itertools import combinations


def d11parse(data):
    max_y = len(data)
    max_x = len(data[0])

    # find the cosmic growth lines
    add_lines = []
    for i in range(len(data)):
        line = data[i]
        if '#' not in line:
            add_lines.append(i)

    # find the cosmic growth columns
    add_rows = []
    for i in range(len(data[0])):
        hash_number = 0
        for j in range(len(data)):
            if data[j][i] == '#':
                hash_number += 1

        if hash_number == 0:
            add_rows.append(i)

    # create a list containing all galaxy pairs
    galaxies = set()
    for y in range(max_y):
        for x in range(max_x):
            if data[y][x] == '#':
                galaxies.add((y, x))

    galaxy_pairs = set(combinations(galaxies, 2))

    return (galaxy_pairs, add_lines, add_rows)


def get_result(galaxy_pairs, add_lines, add_rows, galaxy_growth):
    """
    calculate the expected result by taking into account galaxy growth
    """
    result = 0
    for pair in galaxy_pairs:
        p = iter(pair)
        galaxy1 = next(p)
        galaxy2 = next(p)

        y1, x1 = galaxy1
        y2, x2 = galaxy2

        xmax = max(x1, x2)
        ymax = max(y1, y2)
        xmin = min(x1, x2)
        ymin = min(y1, y2)

        distance = xmax + ymax - xmin - ymin
        for y in add_lines:
            if ymin < y < ymax:
                distance += galaxy_growth - 1
        for x in add_rows:
            if xmin < x < xmax:
                distance += galaxy_growth - 1

        result += distance

    return result


def d11p1(data):
    """
    You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.
    He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.
    Maybe you can help him with the analysis to speed things up?
    The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....

    The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.
    Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.
    In the above example, three columns and two rows contain no galaxies:

       v  v  v
     ...#......
     .......#..
     #.........
    >..........<
     ......#...
     .#........
     .........#
    >..........<
     .......#..
     #...#.....
       ^  ^  ^

    These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

    ....#........
    .........#...
    #............
    .............
    .............
    ........#....
    .#...........
    ............#
    .............
    .............
    .........#...
    #....#.......

    Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

    ....1........
    .........2...
    3............
    .............
    .............
    ........4....
    .5...........
    ............6
    .............
    .............
    .........7...
    8....9.......

    In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)
    For example, here is one of the shortest paths between galaxies 5 and 9:

    ....1........
    .........2...
    3............
    .............
    .............
    ........4....
    .5...........
    .##.........6
    ..##.........
    ...##........
    ....##...7...
    8....9.......

    This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

        Between galaxy 1 and galaxy 7: 15
        Between galaxy 3 and galaxy 6: 17
        Between galaxy 8 and galaxy 9: 5

    In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.
    Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
    """
    galaxy_pairs, add_lines, add_rows = data
    return get_result(galaxy_pairs, add_lines, add_rows, 2)


def d11p2(data):
    """
    The galaxies are much older (and thus much farther apart) than the researcher initially estimated.
    Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.
    (In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)
    Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
    """
    galaxy_pairs, add_lines, add_rows = data
    return get_result(galaxy_pairs, add_lines, add_rows, 1000000)
