"""
aoc y2023 day 7
https://adventofcode.com/2023/day/7
"""
from copy import deepcopy

card_values = {
    'X': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


def hand_value(hand):
    """
    return the card hand in a list format using the int card value
    :return list[int]: return a "A2345" hand in format [14, 2, 3, 4, 5]
    """
    return [card_values[card] for card in hand]


def hand_type(hand):
    """
    get the correct hand type from a hand (ex: AAAAA is a five_kinds, AAA22 a full house etc)
    :return str: the hand type
    """
    # count each card type in hand
    card_count = {card: 0 for card in card_values.keys()}
    for i in range(5):
        card_count[hand[i]] += 1

    # find hand type based on card types
    max_card_number = 0
    type_ = 'high_cards'
    for card_number in card_count.values():
        max_card_number = card_number if card_number > max_card_number else max_card_number

    if max_card_number == 5:
        type_ = 'five_kinds'

    if max_card_number == 4:
        type_ = 'four_kinds'
        # account for joker
        if card_count['X'] == 4:
            type_ = 'five_kinds'
        if card_count['X'] == 1:
            type_ = 'five_kinds'

    if max_card_number == 3:
        type_ = 'three_kinds'
        another_pair = False
        for card_number_2 in card_count.values():
            if card_number_2 == 2:
                another_pair = True

        if another_pair:
            type_ = 'full_houses'
            if card_count['X'] >= 2:
                type_ = 'five_kinds'
            if card_count['X'] == 1:
                type_ = 'four_kinds'
        else:
            if card_count['X'] > 0:
                type_ = 'four_kinds'

    if max_card_number == 2:
        type_ = 'pairs'
        number_of_pairs = 0
        for card_number_2 in card_count.values():
            if card_number_2 == 2:
                number_of_pairs += 1

        if number_of_pairs == 2:
            type_ = 'two_pairs'
            if card_count['X'] == 2:
                type_ = 'four_kinds'
            if card_count['X'] == 1:
                type_ = 'full_houses'
        else:
            type_ = 'pairs'
            if card_count['X'] != 0:
                type_ = 'three_kinds'

    if max_card_number == 1 and card_count['X'] == 1:
        type_ = 'pairs'

    return type_


def parse_hand(line):
    """
    return a line from the input into a parsed dict with the correct hand_type (pair, three of a kind etc)
    :return dict: the parsed line
    """
    split_line = line.split()
    hand = split_line[0]
    bid_value = int(split_line[1])

    parsed_hand = {
        'hand': hand,
        'bid': bid_value,
        'hand_value': hand_value(hand),
        'hand_type': hand_type(hand)
    }

    return parsed_hand


def d7parse(data):
    """
    parse
    """
    hands = {
        'high_cards': [],
        'pairs': [],
        'two_pairs': [],
        'three_kinds': [],
        'full_houses': [],
        'four_kinds': [],
        'five_kinds': []
    }
    # Make another copy of the hands list to parse it correctly for part 2
    hands_p2 = deepcopy(hands)
    for line in data:
        hand = parse_hand(line)
        hands[hand['hand_type']].append(hand)

        # for part 2
        hand_p2 = parse_hand(line.replace('J', 'X'))
        hands_p2[hand_p2['hand_type']].append(hand_p2)

    return {
        'hands': hands,
        'hands_p2': hands_p2
    }


def total_winnings(hands):
    """
    from a hands dict (either hands or hands_p2) return the sum of (bid * rank) for every hand
    :return int: the expected result
    """
    result = 0
    rank = 1
    for key, values in hands.items():
        sorted_values = sorted(values, key=lambda x: x['hand_value'])
        # print(key)

        for hand in sorted_values:
            hand_value = hand['bid'] * rank
            result += hand_value
            # print(f'  rank: {rank}, result: {result}, hand: {hand}, hand value: {hand_value}')
            rank += 1

    return result

def d7p1(data):
    """
    part 1
    """
    hands = data['hands']
    return total_winnings(hands)


def d7p2(data):
    """
    part 2
    """
    hands_p2 = data['hands_p2']
    return total_winnings(hands_p2)
