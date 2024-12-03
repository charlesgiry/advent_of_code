"""
aoc y2023 day 5
https://adventofcode.com/2023/day/5
"""


def d5parse(data: list[str]):
    """
    parse
    """
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
    part 1
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
    part 2

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
