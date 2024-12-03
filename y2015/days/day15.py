"""
aoc y2015 day 15
https://adventofcode.com/2015/day/15
"""


class Ingredient:
    """

    """
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __init__(self, n, c, d, f, t, cal):
        """

        """
        self.name = n
        self.capacity = c
        self.durability = d
        self. flavor = f
        self.texture = t
        self.calories = cal

    def __repr__(self):
        """

        """
        return self.name


def d15parse(data):
    """
    parse
    """
    ingredients = []
    for line in data:
        split_line = line.split()
        name = split_line[0][:-1].lower()
        capacity = int(split_line[2][:-1])
        durability = int(split_line[4][:-1])
        flavor = int(split_line[6][:-1])
        texture = int(split_line[8][:-1])
        calories = int(split_line[-1])

        ingredient = Ingredient(name, capacity, durability, flavor, texture, calories)
        ingredients.append(ingredient)
    return ingredients


def get_score(ingredients, number_of_ingredients):
    """

    """
    capacity = sum([ingredients[i].capacity * number_of_ingredients[i] for i in range(len(ingredients))])
    durability = sum([ingredients[i].durability * number_of_ingredients[i] for i in range(len(ingredients))])
    flavor = sum([ingredients[i].flavor * number_of_ingredients[i] for i in range(len(ingredients))])
    texture = sum([ingredients[i].texture * number_of_ingredients[i] for i in range(len(ingredients))])

    if any(part <= 0 for part in[capacity, durability, flavor, texture]):
        return 0

    return capacity * durability * flavor * texture


def d15p1(data):
    """
    part 1
    """
    result = 0
    for ingredient_1 in range(100):
        for ingredient_2 in range(0, 100 - ingredient_1):
            for ingredient_3 in range(0, 100 - ingredient_1 - ingredient_2):
                ingredient_4 = 100 - ingredient_1 - ingredient_2 - ingredient_3

                number_of_ingredients = [ingredient_1, ingredient_2, ingredient_3, ingredient_4]
                score = get_score(data, number_of_ingredients)
                if score > result:
                    result = score

    return result


def d15p2(data):
    """
    part 2
    """
    result = 0
    for ingredient_1 in range(100):
        for ingredient_2 in range(0, 100 - ingredient_1):
            for ingredient_3 in range(0, 100 - ingredient_1 - ingredient_2):
                ingredient_4 = 100 - ingredient_1 - ingredient_2 - ingredient_3
                number_of_ingredients = [ingredient_1, ingredient_2, ingredient_3, ingredient_4]
                calories = sum([data[i].calories * number_of_ingredients[i] for i in range(len(data))])
                if not calories == 500:
                    continue
                score = get_score(data, number_of_ingredients)
                if score > result:
                    result = score
    return result
