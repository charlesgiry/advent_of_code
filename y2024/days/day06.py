"""
aoc y2024 day 06
https://adventofcode.com/2024/day/6
"""
from numpy import array, argwhere

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def d6parse(data):
    """
    parse
    """
    arr = array([list(line) for line in data], dtype='U1')
    startpos = tuple(int(i) for i in argwhere(arr == '^')[0])
    obstacles = set()
    for elem in argwhere(arr == '#'):
        obstacles.add(tuple(int(i) for i in elem))

    return {
        'arr': arr,
        'startpos': startpos,
        'obstacles': obstacles,
    }


def d6p1(data):
    """
    part 1
    """
    arr = data['arr']
    startpos = data['startpos']
    obstacles = data['obstacles']
    max_x = arr.shape[1]
    max_y = arr.shape[0]
    current_dir = UP
    visited = set()
    y, x = startpos

    while (0 < x < max_x-1) and (0 < y < max_y-1):
        met_obstacle = False
        for obstacle in obstacles:
            if current_dir == UP and obstacle[1] == x and obstacle[0] < y:
                for i in range(y, obstacle[0], -1):
                    visited.add((i, x))
                    arr[i][x] = '^'
                y = obstacle[0] + 1
                current_dir = RIGHT
                met_obstacle = True
                # for line in arr:
                #     str = ''.join(line)
                #     print(str)
                # print('--------------------------------')
                # print('')

            elif current_dir == RIGHT and obstacle[0] == y and obstacle[1] > x:
                for i in range(x, obstacle[1]):
                    visited.add((y, i))
                    arr[y][i] = '>'
                x = obstacle[1] - 1
                current_dir = DOWN
                met_obstacle = True
                # for line in arr:
                #     str = ''.join(line)
                #     print(str)
                # print('--------------------------------')
                # print('')

            elif current_dir == DOWN and obstacle[1] == x and obstacle[0] > y:
                for i in range(y, obstacle[0]):
                    visited.add((i, x))
                    arr[i][x] = 'v'
                y = obstacle[0] - 1
                current_dir = LEFT
                met_obstacle = True
                # for line in arr:
                #     str = ''.join(line)
                #     print(str)
                # print('--------------------------------')
                # print('')

            elif current_dir == LEFT and obstacle[0] == y and obstacle[1] < x:
                for i in range(x, obstacle[1], -1):
                    visited.add((y, i))
                    arr[y][i] = '<'
                x = obstacle[1] + 1
                current_dir = UP
                met_obstacle = True
                # for line in arr:
                #     str = ''.join(line)
                #     print(str)
                # print('--------------------------------')
                # print('')

        if not met_obstacle:
            if current_dir == UP:
                for i in range(y, -1, -1):
                    visited.add((i, x))
                    arr[i][x] = '^'
                y = 0

            elif current_dir == RIGHT:
                for i in range(x, max_x):
                    visited.add((y, i))
                    arr[y][i] = '>'
                x = max_x

            elif current_dir == DOWN:
                for i in range(y, max_y):
                    visited.add((i, x))
                    arr[i][x] = 'v'
                y = max_y

            else:
                for i in range(x, -1, -1):
                    visited.add((y, i))
                    arr[y][i] = '<'
                x = 0

    
    # for line in arr:
    #     str = ''.join(line)
    #     print(str)

    return len(visited)


def d6p2(data):
    """
    part 2
    """
    pass


if __name__ == '__main__':
    data = open('../data/day06.txt', 'r').read().splitlines()
    data = d6parse(data)
    r1 = d6p1(data)
    r2 = d6p2(data)

    print(r1, r2)