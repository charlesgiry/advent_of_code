"""
aoc y2023 day 5
https://adventofcode.com/2023/day/5
"""


def d5parse(data: list[str]):
    current = ''
    seeds = []
    almanac = {
        'seed-to-soil map': [],
        'soil-to-fertilizer map': [],
        'fertilizer-to-water map': [],
        'water-to-light map': [],
        'light-to-temperature map': [],
        'temperature-to-humidity map': [],
        'humidity-to-location map': []
    }
    for line in data:
        split_line = line.split(':')
        if len(split_line) == 2:
            current = split_line[0]

            if current == 'seeds':
                data = split_line[1]
                seeds = [int(i) for i in data.split()]

        if line != '' and line[0].isdigit():
            data = line.split()
            line_repr = {
                'min': int(data[1]),
                'max': int(data[1]) + int(data[2]) - 1,
                'target_min': int(data[0]),
                'target_max': int(data[0]) + int(data[2]) - 1,
                'func': int(data[0]) - int(data[1])
            }
            almanac[current].append(line_repr)

    return {
        'seeds': seeds,
        'almanac': almanac
    }

def d5p1(data):
    """
    You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.
    "A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.
    "Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few y2023... weeks... oh no." His face sinks into a look of horrified realization.
    "I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"
    You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."
    The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

    For example:

    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4

    The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.
    The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.
    Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.
    Consider again the example seed-to-soil map:

    50 98 2
    52 50 48

    The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.
    The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.
    Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.
    So, the entire list of seed numbers and their corresponding soil numbers looks like this:

    seed  soil
    0     0
    1     1
    ...   ...
    48    48
    49    49
    50    52
    51    53
    ...   ...
    96    98
    97    99
    98    50
    99    51

    With this map, you can look up the soil number required for each initial seed number:

        Seed number 79 corresponds to soil number 81.
        Seed number 14 corresponds to soil number 14.
        Seed number 55 corresponds to soil number 57.
        Seed number 13 corresponds to soil number 13.

    The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

        Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
        Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
        Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
        Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

    So, the lowest location number in this example is 35.
    What is the lowest location number that corresponds to any of the initial seed numbers?
    """
    seeds = data['seeds']
    almanac = data['almanac']
    min_value = max(seeds)
    for seed in seeds:
        current_value = seed
        for key, value in almanac.items():
            for elem in value:
                if elem['min'] <= current_value <= elem['max']:
                    current_value += elem['func']
                    break

        if min_value > current_value:
            min_value = current_value

    return min_value


def d5p2(data):
    """
    Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.
    The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

    seeds: 79 14 55 13

    This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.
    Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.
    In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.
    Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

    Damn, spent 6,hours debugging a stupid typo
    """
    seeds = data['seeds']
    almanac = data['almanac']
    seed_ranges = []
    results = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append([seeds[i], seeds[i] + seeds[i+1]])

    for seed_range in seed_ranges:
        current_range = [seed_range]
        # print(f'seed: {current_range}')

        next_range = []
        for key, steps in almanac.items():
            # print(f'  key: {key}')
            next_range = []
            while current_range:
                transform = False
                range_to_transform = current_range.pop(0)
                # print(f'    current range: {range_to_transform}')
                for step in steps:
                    # range is 100% in
                    if step['min'] <= range_to_transform[0] <= range_to_transform[1] <= step['max']:
                        # print(f'      step: {step}')
                        tranformed_range = [
                            range_to_transform[0] + step['func'],
                            range_to_transform[1] + step['func']
                        ]
                        next_range.append(tranformed_range)
                        # print(f'        totally within: {tranformed_range}')
                        transform = True
                        break

                    # part of the range is smaller, rest in in
                    elif range_to_transform[0] < step['min'] <= range_to_transform[1] <= step['max']:
                        # print(f'      step: {step}')
                        new_range = [
                            range_to_transform[0],
                            step['min'] - 1
                        ]
                        transformed_range = [
                            step['min'] + step['func'],
                            range_to_transform[1] + step['func']
                        ]
                        current_range.append(new_range)
                        next_range.append(transformed_range)
                        # print(f'        part small {new_range}, part within {transformed_range}')
                        transform = True
                        break

                    # part off the range is in, rest is bigger
                    elif step['min'] <= range_to_transform[0] <= step['max'] < range_to_transform[1]:
                        # print(f'      step: {step}')
                        transformed_range = [
                            range_to_transform[0] + step['func'],
                            step['max'] + step['func']
                        ]
                        new_range = [
                            step['max'] + 1,
                            range_to_transform[1]
                        ]

                        next_range.append(transformed_range)
                        current_range.append(new_range)
                        # print(f'        part within {transformed_range}, part big {new_range}')
                        transform = True
                        break

                    # part is too small, part is in, part is too big
                    elif range_to_transform[0] <= step['min'] <= step['max'] <= range_to_transform[1]:
                        # print(f'      step: {step}')
                        new_range_small = [
                            range_to_transform[0],
                            step['min'] - 1
                        ]

                        transformed_range = [
                            step['min'] + step['func'],
                            step['max'] + step['func']
                        ]

                        new_range_big = [
                            step['max'] + 1,
                            range_to_transform[1]
                        ]

                        current_range.append(new_range_small)
                        next_range.append(transformed_range)
                        current_range.append(new_range_big)
                        # print(f'        part small {new_range_small}, part within {transformed_range}, part big {new_range_big}')
                        transform = True
                        break

                if not transform:
                    # print(f'      step: {step}')
                    next_range.append(range_to_transform)
                    # print(f'    totally out {range_to_transform}')

                # print('')

            # print(f'  next step: {next_range}')
            # print('')
            current_range = next_range

        results += next_range


    min = max(seeds)
    for result in results:
        for res in result:
            min = min if res > min else res

    # print(f'result: {min}')
    return min
