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
    obstacles = {
        'x': {},
        'y': {}
    }
    for elem in argwhere(arr == '#'):
        y = int(elem[0])
        x = int(elem[1])

        if x not in obstacles['x']:
            obstacles['x'][x] = []

        if y not in obstacles['y']:
            obstacles['y'][y] = []

        obstacles['x'][x].append(y)
        obstacles['y'][y].append(x)

    for key, values in obstacles['x'].items():
        obstacles['x'][key] = sorted(values)

    return {
        'arr': arr,
        'startpos': startpos,
        'obstacles': obstacles,
    }


def walk(arr, current_pos, current_dir):
    walked = set()
    walked.add((current_pos, current_dir))

    max_x = arr.shape[1]
    max_y = arr.shape[0]
    y, x = current_pos

    while (0 < x < max_x-1 and 0 < y < max_y-1):
        if current_dir == UP:
            if arr[y-1, x] == '#':
                current_dir = RIGHT
            else:
                y -= 1

        elif current_dir == RIGHT:
            if arr[y, x+1] == '#':
                current_dir = DOWN
            else:
                x += 1

        elif current_dir == DOWN:
            if arr[y+1, x] == '#':
                current_dir = LEFT
            else:
                y += 1

        elif current_dir == LEFT:
            if arr[y, x-1] == '#':
                current_dir = UP
            else:
                x -= 1

        combo = ((y, x), current_dir)
        if combo in walked:
            return walked, True
        else:
            walked.add(combo)
    return walked, False


def d6p1(data):
    """
    move 1 by 1
    """
    arr = data['arr']
    start_pos = data['startpos']
    start_dir = UP

    path, looped = walk(arr, start_pos, start_dir)


    result = set()
    for elem in path:
        result.add(elem[0])
    return len(result)


def d6p2(data):
    """
    part 2
    still broken
    """
    arr = data['arr']
    start_pos = data['startpos']
    start_dir = UP
    result = 0
    path, _ = walk(arr, start_pos, start_dir)

    for point in path:
        arr[point[0], point[1]] = '#'
        _, loop = walk(arr, start_pos, start_dir)
        arr[point[0], point[1]] = '.'
        if loop:
            result += 1
    return result


if __name__ == '__main__':
    # borrowed from https://www.reddit.com/r/adventofcode/comments/1h7tovg/comment/m0o5xe4/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    # will check why my code don't work later
    G = {i + j * 1j: c for i, r in enumerate(open('../data/day06.txt'))
         for j, c in enumerate(r.strip())}
    start = min(p for p in G if G[p] == '^')
    def walk(G):
        pos, dir, seen = start, -1, set()
        while pos in G and (pos, dir) not in seen:
            seen |= {(pos, dir)}
            if G.get(pos + dir) == "#":
                dir *= -1j
            else:
                pos += dir
        return {p for p, _ in seen}, (pos, dir) in seen
    path = walk(G)[0]
    print(len(path),
          sum(walk(G | {o: '#'})[1] for o in path))
