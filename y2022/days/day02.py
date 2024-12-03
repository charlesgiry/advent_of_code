"""
aoc y2022 day 02
https://adventofcode.com/2022/day/2
"""

class Hand:
    """

    """
    type: str
    value: int

    def __init__(self, character):
        """

        """
        if character in ['A', 'X', 'ROCK']:
            self.type = 'ROCK'
            self.value = 1
        elif character in ['B', 'Y', 'PAPER']:
            self.type = 'PAPER'
            self.value = 2
        else:
            self.type = 'SCISSORS'
            self.value = 3

    def loses_to(self):
        """

        """
        if self.type == 'ROCK':
            return 'PAPER'
        elif self.type == 'PAPER':
            return 'SCISSORS'
        else:
            return 'ROCK'

    def wins_to(self):
        """

        """
        if self.type == 'ROCK':
            return 'SCISSORS'
        elif self.type == 'PAPER':
            return 'ROCK'
        else:
            return 'PAPER'


    def __gt__(self, other):
        """
        implements hand1 > hand2
        """
        return other.loses_to() == self.type


    def __eq__(self, other):
        """
        implement hand1 == hand2
        """
        return self.type == other.type


def d2parse(data):
    """
    parse
    """
    result = []
    for line in data:
        result.append([
            Hand(line[0]),
            Hand(line[2]),
            line[2]
        ])
    return result


def d2p1(data):
    """
    part 1
    """
    result = 0
    for round in data:
        opponent, player, _ = round
        result += player.value

        if player > opponent:
            result += 6

        elif player == opponent:
            result += 3

    return result


def d2p2(data):
    """
    part 2
    """
    result = 0
    for round in data:
        opponent, _, target = round
        # lose
        if target == 'X':
            player = Hand(opponent.wins_to())
        # Draw
        elif target == 'Y':
            player = Hand(opponent.type)
            result += 3
        # Win
        else:
            player = Hand(opponent.loses_to())
            result += 6

        result += player.value


    return result
