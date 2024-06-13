"""
aoc y2023 day 18
https://adventofcode.com/2023/day/18
"""
from re import compile


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def d18parse(data):
    lines = []
    for line in data:
        parsed_line = {}
        # R 6 (#70c710)
        split_line = line.split()
        match split_line[0]:
            case 'R':
                parsed_line['dir'] = RIGHT
            case 'D':
                parsed_line['dir'] = DOWN
            case 'L':
                parsed_line['dir'] = LEFT
            case 'U':
                parsed_line['dir'] = UP

        parsed_line['len'] = int(split_line[1])
        parsed_line['hex'] = split_line[2][1:-1]

        lines.append(parsed_line)
    return lines


def get_edges(input_data):
    """
    Get all the edges of a polygon from parsed puzzle data
    """
    x = 0
    y = 0
    edges = []
    for data in input_data:
        ym, xm = data['dir']
        new_y = y + (ym * data['len'])
        new_x = x + (xm * data['len'])

        edge = ((y, x), (new_y, new_x))
        y = new_y
        x = new_x
        edges.append(edge)

    return edges


def shoelace(edges):
    """
    Shoelace formula that also takes into account the edges themselves, not just the content
    """
    side_len = 0
    area = 0
    for edge in edges:
        pos1, pos2 = edge
        y1, x1 = pos1
        y2, x2 = pos2
        side_len += (max(y2, y1) - min(y2, y1)) + (max(x2, x1) - min(x2, x1))
        area += (y1 * x2) - (x1 * y2)

    area = ((abs(area) + side_len) // 2) + 1
    return area


def d18p1(data):
    """
    Thanks to your efforts, the machine parts factory is one of the first factories up and running since the lavafall came back. However, to catch up with the large backlog of parts requests, the factory will also need a large supply of lava for a while; the Elves have already started creating a large lagoon nearby for this purpose.
    However, they aren't sure the lagoon will be big enough; they've asked you to take a look at the dig plan (your puzzle input). For example:

    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)

    The digger starts in a 1 meter cube hole in the ground. They then dig the specified number of meters up (U), down (D), left (L), or right (R), clearing full 1 meter cubes as they go. The directions are given as seen from above, so if "up" were north, then "right" would be east, and so on. Each trench is also listed with the color that the edge of the trench should be painted as an RGB hexadecimal color code.
    When viewed from above, the above example dig plan would result in the following loop of trench (#) having been dug out from otherwise ground-level terrain (.):

    #######
    #.....#
    ###...#
    ..#...#
    ..#...#
    ###.###
    #...#..
    ##..###
    .#....#
    .######

    At this point, the trench could contain 38 cubic meters of lava. However, this is just the edge of the lagoon; the next step is to dig out the interior so that it is one meter deep as well:

    #######
    #######
    #######
    ..#####
    ..#####
    #######
    #####..
    #######
    .######
    .######

    Now, the lagoon can contain a much more respectable 62 cubic meters of lava. While the interior is dug out, the edges are also painted according to the color codes in the dig plan.
    The Elves are concerned the lagoon won't be large enough; if they follow their dig plan, how many cubic meters of lava could it hold?
    """
    edges = get_edges(data)
    cubic_meter = shoelace(edges)
    return cubic_meter


def d18p2(data):
    """
    The Elves were right to be concerned; the planned lagoon would be much too small.
    After a few minutes, someone realizes what happened; someone swapped the color and instruction parameters when producing the dig plan. They don't have time to fix the bug; one of them asks if you can extract the correct instructions from the hexadecimal codes.
    Each hexadecimal code is six hexadecimal digits long. The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number. The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.
    So, in the above example, the hexadecimal codes can be converted into the true instructions:

        #70c710 = R 461937
        #0dc571 = D 56407
        #5713f0 = R 356671
        #d2c081 = D 863240
        #59c680 = R 367720
        #411b91 = D 266681
        #8ceee2 = L 577262
        #caa173 = U 829975
        #1b58a2 = L 112010
        #caa171 = D 829975
        #7807d2 = L 491645
        #a77fa3 = U 686074
        #015232 = L 5411
        #7a21e3 = U 500254

    Digging out this loop and its interior produces a lagoon that can hold an impressive 952408144115 cubic meters of lava.
    Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, how many cubic meters of lava could the lagoon hold?
    """
    # parse the line using the hex as expected
    converted_lines = []
    for line in data:
        parsed_hex = {
            'len': int(line['hex'][1:-1], base=16)
        }
        dir_ = line['hex'][-1]
        if dir_ == '0':
            parsed_hex['dir'] = RIGHT
        elif dir_ == '1':
            parsed_hex['dir'] = DOWN
        elif dir_ == '2':
            parsed_hex['dir'] = LEFT
        else:
            parsed_hex['dir'] = UP
        converted_lines.append(parsed_hex)

    # get the edges of the polygon
    edges = get_edges(converted_lines)

    # calculate the surface of the polygon
    area = shoelace(edges)
    return area
