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
    """
    parse
    """
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
    part 1
    """
    edges = get_edges(data)
    cubic_meter = shoelace(edges)
    return cubic_meter


def d18p2(data):
    """
    part 2
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
