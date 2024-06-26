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
    r"""
    With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility.
    At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave,
    and the floor is cave, and you're pretty sure this is actually just a giant cave.
    Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead.
    There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility
    and pouring all of its energy into a contraption on the opposite side.
    Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid
    containing empty space (.), mirrors (/ and \), and splitters (| and -).
    The contraption is aligned so that most of the beam bounces around the grid,
    but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.
    You note the layout of the contraption (your puzzle input). For example:

    .|...\....
    |.-.\.....
    .....|-...
    ........|.
    ..........
    .........\
    ..../.\\..
    .-.-/..|..
    .|....-|.\
    ..//.|....

    The beam enters in the top-left corner from the left and heading to the right.
    Then, its behavior depends on what it encounters as it moves:

        If the beam encounters empty space (.), it continues in the same direction.
        If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
        If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
        If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.

    Beams do not interact with other beams; a tile can have many beams passing through it at the same time.
    A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.
    In the above example, here is how the beam of light bounces around the contraption:

    >|<<<\....
    |v-.\^....
    .v...|->>>
    .v...v^.|.
    .v...v^...
    .v...v^..\
    .v../2\\..
    <->-/vv|..
    .|<<<2-|.\
    .v//.|.v..

    Beams are only shown on empty tiles; arrows indicate the direction of the beams.
    If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead.
    Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

    ######....
    .#...#....
    .#...#####
    .#...##...
    .#...##...
    .#...##...
    .#..####..
    ########..
    .#######..
    .#...#.#..

    Ultimately, in this example, 46 tiles become energized.
    The light isn't energizing enough tiles to produce lava; to debug the contraption,
    you need to start by analyzing the current situation. With the beam starting in the top-left heading right,
    how many tiles end up being energized?
    """
    max_y = len(data)
    max_x = len(data[0])
    return move_rays(data, 0, 0, max_y, max_x, RIGHT)


def d16p2(data):
    r"""
    As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel.
    There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile
    and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner;
    for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)
    So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward),
    any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left).
    To produce lava, you need to find the configuration that energizes as many tiles as possible.
    In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

    .|<2<\....
    |v-v\^....
    .v.v.|->>>
    .v.v.v^.|.
    .v.v.v^...
    .v.v.v^..\
    .v.v/2\\..
    <-2-/vv|..
    .|<<<2-|.\
    .v//.|.v..

    Using this configuration, 51 tiles are energized:

    .#####....
    .#.#.#....
    .#.#.#####
    .#.#.##...
    .#.#.##...
    .#.#.##...
    .#.#####..
    ########..
    .#######..
    .#...#.#..

    Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?
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
