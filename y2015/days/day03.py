"""
aoc y2015 day 3
https://adventofcode.com/2015/day/3
"""


def d3parse(data):
    """
    As data is a list of all the lines in the file, and the file only contains 1 line
    return the first element of data as data
    """
    return data[0]


def d3p1(data):
    """
    part 1
    """
    x = 0
    y = 0
    visited = set()
    visited.add((x, y))

    for move in data:
        if move == '<':
            x -= 1
        elif move == '>':
            x += 1
        elif move == 'v':
            y -= 1
        else:
            y += 1

        current = (x, y)
        visited.add(current)

    return len(visited)


class Santa:
    """

    """
    x: int
    y: int

    def __init__(self):
        """

        """
        self.x = 0
        self.y = 0

    def move(self, direction):
        """

        """
        if direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1
        elif direction == 'v':
            self.y -= 1
        else:
            self.y += 1
        return (self.x, self.y)


def d3p2(data):
    """
    part 2
    """
    data_as_list = list(data)
    visited_by_santa = data_as_list[::2]
    visited_by_robot = data_as_list[1::2]
    assert len(visited_by_robot) == len(visited_by_santa)

    visited = set()
    santa = Santa()
    robot = Santa()
    for i in range(len(visited_by_santa)):
        visited.add(santa.move(visited_by_santa[i]))
        visited.add(robot.move(visited_by_robot[i]))

    return len(visited)
