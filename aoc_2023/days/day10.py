"""
aoc 2023 day 10
https://adventofcode.com/2023/day/10
"""
# import matplotlib.pyplot as plt
#
# def draw_polygon(points, single_point=None):
#     # Extract y and x coordinates from the list of points
#     y_coordinates, x_coordinates = zip(*points)
#
#     # Close the polygon by connecting the last point to the first point
#     y_coordinates += (y_coordinates[0],)
#     x_coordinates += (x_coordinates[0],)
#
#     # Plot the polygon
#     plt.plot(x_coordinates, y_coordinates, marker='o', linestyle='-', label='Polygon')
#     plt.fill(x_coordinates, y_coordinates, alpha=0.3)  # Fill the polygon
#
#     # Plot a single point if provided
#     if single_point:
#         y_single, x_single = single_point
#         plt.plot(x_single, y_single, marker='o', color='red', label='Single Point')
#
#     # Set labels and display the legend
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Polygon with Single Point')
#     plt.grid(True)
#     plt.legend()
#     plt.show()


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

with open('data/day10_data.txt', 'r') as file:
    lines = file.read().splitlines()
    max_y, max_x = len(lines), len(lines[0])


def find_neighbours(pos: tuple[int, int]):
    """
    return all the neighbours of a position that are within the map
    """
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


def valid_neighbours(pos):
    """
    return the valid neighbour of a pipe given its value
    """
    (y, x) = pos
    pipe = lines[y][x]
    neighbours = set()
    possibilities = pipe_connections[pipe]
    possible_neighbours = find_neighbours(pos)

    for neighbour in possible_neighbours:
        ny, nx = neighbour
        diff = (ny-y, nx-x)
        neighbour_pipe = lines[ny][nx]

        if diff in possibilities:
            if neighbour_pipe in possibilities[diff]:
                neighbours.add(neighbour)
    return neighbours


def find_start_type(start: tuple[int, int]):
    """
    Find what's the value of the start pipe
    """
    (y, x) = start
    pipe_types = [
        '|', '-', 'L', 'J', '7', 'F'
    ]
    start_type = 'S'

    for pipe in pipe_types:
        lines[y] = lines[y][:x] + pipe + lines[y][x+1:]
        neighbours = valid_neighbours(start)
        if len(neighbours) == 2:
            start_type = pipe

    lines[y] = lines[y][:x] + 'S' + lines[y][x+1:]
    return start_type


def walk_pipes(start: tuple[int, int]):
    """
    from a starting point (transformed from S to its actual value) walk the closed loop
    return the closed loop
    """
    current = start
    # use a set to ensure you don't walk a point twice to avoid infinite loops
    # return the form as an array as the set reorders the points
    walked_paths = {start}
    form = [start]
    neighbours = valid_neighbours(start) - walked_paths

    while len(neighbours) > 0:
        current = neighbours.pop()
        walked_paths.add(current)
        form.append(current)
        neighbours = valid_neighbours(current) - walked_paths

    return form


def ray_casting_is_inside(point, form):
    """
    fire a "ray" from pos, from left to right, and if the ray crosses
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


start = (0, 0)
for y in range(max_y):
    for x in range(max_x):
        if lines[y][x] == 'S':
            start = (y, x)

# replace the starting position with its actual value
start_type = find_start_type(start)
y, x = start
lines[y] = lines[y][:x] + start_type + lines[y][x + 1:]

# find the expected result
pipes = walk_pipes(start)

def d10p1():
    """
    You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.
    You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.
    The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.
    Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).
    The pipes are arranged in a two-dimensional grid of tiles:

        | is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
        . is ground; there is no pipe in this tile.
        S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is one large, continuous loop.
    For example, here is a square loop of pipe:

    .....
    .F-7.
    .|.|.
    .L-J.
    .....

    If the animal had entered this loop in the northwest corner, the sketch would instead look like this:

    .....
    .S-7.
    .|.|.
    .L-J.
    .....

    In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.
    Unfortunately, there are also many pipes that aren't connected to the loop! This sketch shows the same loop as above:

    -L|F7
    7S-7|
    L|7||
    -L-J|
    L|-JF

    In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to S, pipes those pipes connect to, pipes those pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including S, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).
    Here is a sketch that contains a slightly more complex main loop:

    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...

    Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:

    7-F7-
    .FJ|7
    SJLL7
    |F--J
    LJ.LJ

    If you want to get out ahead of the animal, you should find the tile in the loop that is farthest from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.
    In the first example with the square loop:

    .....
    .S-7.
    .|.|.
    .L-J.
    .....

    You can count the distance each tile in the loop is from the starting point like this:

    .....
    .012.
    .1.3.
    .234.
    .....

    In this example, the farthest point from the start is 4 steps away.
    Here's the more complex loop again:

    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...

    Here are the distances for each tile on that loop:

    ..45.
    .236.
    01.78
    14567
    23...

    Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?
    """
    result = int(len(pipes) / 2)
    return result


def d10p2():
    """
    You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?
    To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

    ...........
    .S-------7.
    .|F-----7|.
    .||.....||.
    .||.....||.
    .|L-7.F-J|.
    .|..|.|..|.
    .L--J.L--J.
    ...........

    The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

    ...........
    .S-------7.
    .|F-----7|.
    .||OOOOO||.
    .||OOOOO||.
    .|L-7OF-J|.
    .|II|O|II|.
    .L--JOL--J.
    .....O.....

    In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

    ..........
    .S------7.
    .|F----7|.
    .||OOOO||.
    .||OOOO||.
    .|L-7F-J|.
    .|II||II|.
    .L--JL--J.
    ..........

    In both of the above examples, 4 tiles are enclosed by the loop.
    Here's a larger example:

    .F----7F7F7F7F-7....
    .|F--7||||||||FJ....
    .||.FJ||||||||L7....
    FJL7L7LJLJ||LJ.L-7..
    L--J.L7...LJS7F-7L7.
    ....F-J..F7FJ|L7L7L7
    ....L7.F7||L7|.L7L7|
    .....|FJLJ|FJ|F7|.LJ
    ....FJL-7.||.||||...
    ....L---J.LJ.LJLJ...

    The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

    OF----7F7F7F7F-7OOOO
    O|F--7||||||||FJOOOO
    O||OFJ||||||||L7OOOO
    FJL7L7LJLJ||LJIL-7OO
    L--JOL7IIILJS7F-7L7O
    OOOOF-JIIF7FJ|L7L7L7
    OOOOL7IF7||L7|IL7L7|
    OOOOO|FJLJ|FJ|F7|OLJ
    OOOOFJL-7O||O||||OOO
    OOOOL---JOLJOLJLJOOO

    In this larger example, 8 tiles are enclosed by the loop.
    Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJ7F7FJ-
    L---JF-JLJ.||-FJLJJ7
    |F|F-JF---7F7-L7L|7|
    |FFJF7L7F-JF7|JL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L

    Here are just the tiles that are enclosed by the loop marked with I:

    FF7FSF7F7F7F7F7F---7
    L|LJ||||||||||||F--J
    FL-7LJLJ||||||LJL-77
    F--JF--7||LJLJIF7FJ-
    L---JF-JLJIIIIFJLJJ7
    |F|F-JF---7IIIL7L|7|
    |FFJF7L7F-JF7IIL---7
    7-L-JL7||F7|L7F-7F7|
    L.L7LFJ|||||FJL7||LJ
    L7JLJL-JLJLJL--JLJ.L

    In this last example, 10 tiles are enclosed by the loop.
    Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?
    """
    result = 0
    smallest_x = pipes[0][0]
    biggest_x = pipes[0][0]
    smallest_y = pipes[0][1]
    biggest_y = pipes[0][1]

    for pipe in pipes:
        y, x = pipe
        smallest_y = smallest_y if smallest_y < y else y
        biggest_y = biggest_y if biggest_y > y else y
        smallest_x = smallest_x if smallest_x < x else x
        biggest_x = biggest_x if biggest_x > x else x

    pipe_set = set(pipes)

    for y in range(max_y):
        for x in range(max_x):
            if smallest_x < x < biggest_x and smallest_y < y < biggest_y:
                if (y, x) not in pipe_set:
                    if ray_casting_is_inside((y, x), pipes):
                        result += 1

    return result

