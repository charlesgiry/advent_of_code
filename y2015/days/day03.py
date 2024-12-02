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
    Santa is delivering presents to an infinite two-dimensional grid of houses.
    He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
    However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

    For example:
    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
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
    x: int
    y: int

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
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
    The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
    Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
    This year, how many houses receive at least one present?

    For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
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
