"""
aoc y2023 day 16
https://adventofcode.com/2023/day/16
"""


UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


def move_rays(lines, start_y, start_x, max_y, max_x, start_direction):
    """
    Return the number of energized tiles by the ray defined by params
    """
    energized_tiles = set()
    rays = {(start_y, start_x, start_direction)}
    cache = set()

    def move_ray(y, x, direction):
        """
        Check the bounds depending on directions, and add the new ray position to the rays set if within the bounds
        """
        if direction == UP and y - 1 >= 0:
            rays.add((y - 1, x, UP))
        elif direction == LEFT and x - 1 >= 0:
            rays.add((y, x - 1, LEFT))
        elif direction == DOWN and y + 1 < max_y:
            rays.add((y + 1, x, DOWN))
        elif direction == RIGHT and x + 1 < max_x:
            rays.add((y, x + 1, RIGHT))

    while rays:
        ray = rays.pop()
        y, x, direction = ray
        energized_tiles.add((y, x))

        # Move only if we haven't already taken this action in the past to avoid infinite loops and useless calculations
        if (y, x, direction) not in cache:
            cache.add((y, x, direction))

            if lines[y][x] == '.':
                move_ray(y, x, direction)

            elif lines[y][x] == '/':
                direction = UP if direction == RIGHT else LEFT if direction == DOWN else DOWN if direction == LEFT else RIGHT
                move_ray(y, x, direction)

            elif lines[y][x] == '\\':
                direction = UP if direction == LEFT else LEFT if direction == UP else DOWN if direction == RIGHT else RIGHT
                move_ray(y, x, direction)

            elif lines[y][x] == '-':
                if direction == UP or direction == DOWN:
                    move_ray(y, x, LEFT)
                    move_ray(y, x, RIGHT)
                else:
                    move_ray(y, x, direction)

            elif lines[y][x] == '|':
                if direction == LEFT or direction == RIGHT:
                    move_ray(y, x, UP)
                    move_ray(y, x, DOWN)
                else:
                    move_ray(y, x, direction)

    result = len(energized_tiles)
    return result


def d16p1(data):
    """
    part 1
    """
    max_y = len(data)
    max_x = len(data[0])
    return move_rays(data, 0, 0, max_y, max_x, RIGHT)


def d16p2(data):
    """
    part 2
    """
    max_y = len(data)
    max_x = len(data[0])
    results = []

    for y in range(max_y):
        results.append(move_rays(data, y, 0, max_y, max_x, RIGHT))
        results.append(move_rays(data, y, max_x - 1, max_y, max_x, LEFT))

    for x in range(max_x):
        results.append(move_rays(data, 0, x, max_y, max_x, DOWN))
        results.append(move_rays(data, max_y - 1, x, max_y, max_x, UP))

    return max(results)
