"""
aoc y2023 day 10
https://adventofcode.com/2023/day/10
"""
from re import compile

pipe_connections = {
    '|': {
        (-1, 0): ['|', '7', 'F'],
        (1, 0):  ['|', 'L', 'J'],
    },

    '-': {
        (0, -1): ['-', 'L', 'F'],
        (0, 1):  ['-', 'J', '7']
    },

    'L': {
        (0, 1): ['-', 'J', '7'],
        (-1, 0): ['|', 'F', '7']
    },

    'J': {
        (0, -1): ['-', 'L', 'F'],
        (-1, 0): ['|', '7', 'F']
    },

    '7': {
        (0, -1): ['-', 'F', 'L'],
        (1, 0): ['|', 'J', 'L']
    },

    'F': {
        (0, 1): ['-', '7', 'J'],
        (1, 0): ['|', 'L', 'J']
    },
    '.': {
        (-1, 0): ['.'],
        (1, 0): ['.'],
        (0, -1): ['.'],
        (0, 1): ['.']
    }
}


def find_neighbours(pos: tuple[int, int], data):
    """
    return all the neighbours of a position that are within the map
    """
    lines = data['lines']
    max_x = data['max_x']
    max_y = data['max_y']

    y, x = pos
    spot = lines[y][x]
    spots = []

    match spot:
        case '|':
            spots = [(y+1, x), (y-1, x)]
        case '-':
            spots = [(y, x-1), (y, x+1)]
        case 'L':
            spots = [(y-1, x), (y, x+1)]
        case 'J':
            spots = [(y-1, x), (y, x-1)]
        case '7':
            spots = [(y+1, x), (y, x-1)]
        case 'F':
            spots = [(y+1, x), (y, x+1)]
        case '.':
            spots = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    return [(y, x) for (y, x) in spots if y >= 0 and x >= 0 and y < max_y and x < max_x]


def valid_neighbours(pos, data):
    """
    return the valid neighbour of a pipe given its value
    """
    lines = data['lines']

    (y, x) = pos
    pipe = lines[y][x]
    neighbours = set()
    possibilities = pipe_connections[pipe]
    possible_neighbours = find_neighbours(pos, data)

    for neighbour in possible_neighbours:
        ny, nx = neighbour
        diff = (ny-y, nx-x)
        neighbour_pipe = lines[ny][nx]

        if diff in possibilities:
            if neighbour_pipe in possibilities[diff]:
                neighbours.add(neighbour)
    return neighbours


def find_start_type(start: tuple[int, int], data):
    """
    Find what's the value of the start pipe
    """
    lines = data['lines']

    (y, x) = start
    pipe_types = [
        '|', '-', 'L', 'J', '7', 'F'
    ]
    start_type = 'S'

    for pipe in pipe_types:
        lines[y] = lines[y][:x] + pipe + lines[y][x+1:]
        neighbours = valid_neighbours(start, data)
        if len(neighbours) == 2:
            start_type = pipe

    lines[y] = lines[y][:x] + 'S' + lines[y][x+1:]
    return start_type


def walk_pipes(start: tuple[int, int], data):
    """
    from a starting point (transformed from S to its actual value) walk the closed loop
    return the closed loop
    """
    lines = data['lines']

    current = start
    # use a set to ensure you don't walk a point twice to avoid infinite loops
    # return the form as an array as the set reorders the points
    walked_paths = {start}
    form = [start]
    neighbours = valid_neighbours(start, data) - walked_paths

    while len(neighbours) > 0:
        current = neighbours.pop()
        walked_paths.add(current)
        form.append(current)
        neighbours = valid_neighbours(current, data) - walked_paths

    return form, walked_paths


def ray_casting_is_inside(point, form):
    """
    fire a "ray" from pos, from left to right, and if the ray crosses
    Currently not used as using regexp to do the same thing was hugely faster for our specific use
    """
    counter = 0
    y, x = point
    # i and j should be the two points of an edge.
    # to do so, first take the last element and the first element of the form
    # then take the previous element and the current element
    j = len(form) - 1
    for i in range(len(form)):
        # form[i] and form[j] represents a line
        y1, x1 = form[i]
        y2, x2 = form[j]

        # make sure that the point's y is within y1 and y2 so that there can be an intersection
        if y1 <= y < y2 or y2 <= y < y1:
            # cast a ray from left to right
            # calculate the intersection of the ray from (x, y) to the line ((x1, y1), (x2, y2)
            if x < x1 + (((y - y1) / (y2-y1)) * (x2 - x1)):
                counter += 1
        j = i
    # if it crosses the edges of the form an uneven number of times, it's within
    return counter % 2 == 1


def d10parse(data):
    """
    parse
    """
    lines = data
    max_y = len(data)
    max_x = len(data)

    # find the starting position
    start = (0, 0)
    for y in range(max_y):
        for x in range(max_x):
            if lines[y][x] == 'S':
                start = (y, x)

    data_dict = {
        'lines': lines,
        'max_y': max_y,
        'max_x': max_x
    }

    # replace the starting position with its actual value
    start_type = find_start_type(start, data_dict)
    y, x = start
    lines[y] = lines[y][:x] + start_type + lines[y][x + 1:]

    # find the pipe loop
    pipes, pipe_set = walk_pipes(start, data_dict)
    data_dict['pipes'] = pipes
    data_dict['pipe_set'] = pipe_set

    return data_dict


def d10p1(data):
    """
    part 1
    """
    pipes = data['pipes']
    result = int(len(pipes) / 2)
    return result


def d10p2(data):
    """
    part 2
    """
    max_y = data['max_y']
    max_x = data['max_x']
    pipe_set = data['pipe_set']
    lines = data['lines']

    # replace all the characters that are not part of the loop with .
    # then we can count all the pipes left on a line
    for y in range(max_y):
        for x in range(max_x):
            if (y, x) not in pipe_set:
                lines[y] = lines[y][:x] + '.' + lines[y][x+1:]

    # count all intersections with the edges of the pipe loop
    # if the number is uneven, then the character is inside the loop
    result = 0

    # If casting a ray on the right of the character, count |, J and Ls
    # regexp = compile(r'\||J|L')
    # for y in range(max_y):
    #     for x in range(max_x):
    #         if (y, x) not in pipe_set:
    #             found_inter = regexp.findall(lines[y][x:])
    #             if len(found_inter) % 2 == 1:
    #                 result += 1

    # If casting a ray on the left of the character, count |, F or 7s
    regexp = compile(r'\||F|7')
    for y in range(max_y):
        for x in range(max_x):
            if (y, x) not in pipe_set:
                found_inter = regexp.findall(lines[y][:x])
                if len(found_inter) % 2 == 1:
                    result += 1

    return result
