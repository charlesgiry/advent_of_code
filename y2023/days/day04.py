"""
aoc y2023 day 4
https://adventofcode.com/2023/day/4
"""


def parse_line(line):
    """
    return the numbers left and right of the | within sets (for easier comparison
    :param line: line to parse
    :return set, set: winning numbers, game numbers
    """
    parts = line.split(': ')[1].rstrip().split(' | ')
    winning_numbers = set(parts[0].split())
    game_numbers = set(parts[1].split())

    return winning_numbers, game_numbers


def d4p1(data):
    """
    part 1
    """
    result = 0

    for line in data:
        winning_numbers, game_numbers = parse_line(line)
        # since winning_numbers and game_numbers are sets
        # doing a AND will only leave the winning numbers that also were in game_numbers
        power_number = len(winning_numbers & game_numbers)

        if power_number != 0:
            result += pow(2, power_number-1)

    return result


def d4p2(data):
    """
    part 2
    """
    result = 0

    # generate a list containing all the cards at the start
    results = [1 for i in data]

    for i, line in enumerate(data):
        winning_numbers, game_numbers = parse_line(line)
        wins = winning_numbers & game_numbers

        # get current multiplier, and add it to the next cards according to the number of wins
        current_multiplier = results[i]

        # make sure the number of wins don't go over the number of lines
        # (ex you win 10 times on last game, you can't do last game +1)
        for j in range(
                i+1,
                min(i + len(wins) + 1, len(data))
        ):
            results[j] += current_multiplier

        result += current_multiplier

    return result


def d4p2_old(data):
    """
    slightly less efficient version
    keep a lookahead of how many times you have to execute the next cards
    ex:
        game 0: win, win, win
        lookahead = [1, 1, 1]

        game 1: win, win, win
        lookahead at the start = [1, 1, 1]
        get current multiplier: lookahead.pop(0), lookahead = [1, 1]
        add multiplier to all won games
            3 won game: add multiplier to the 2 existing lookahead = [2, 2]
                add a new element to lookahead for 3rd won game: lookahead = [2, 2, 1]
        etc...
    """

    result = 0
    scratchcards = [0]

    for line in data:
        scratchcards = [0] if scratchcards == [] else scratchcards
        scratchcards[0] += 1
        winning_numbers, game_numbers = parse_line(line)
        wins = 0
        for number in game_numbers:
            if number in winning_numbers:
                wins += 1

        multiplier = scratchcards.pop(0)
        result += multiplier
        for i in range(0, wins):
            try:
                scratchcards[i] += multiplier
            except IndexError:
                scratchcards.append(multiplier)

    return result
