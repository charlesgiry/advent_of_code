"""
aoc y2015 day 15
https://adventofcode.com/2015/day/15
"""


class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __init__(self, n, c, d, f, t, cal):
        self.name = n
        self.capacity = c
        self.durability = d
        self. flavor = f
        self.texture = t
        self.calories = cal

    def __repr__(self):
        return self.name


def d15parse(data):
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
    capacity = sum([ingredients[i].capacity * number_of_ingredients[i] for i in range(len(ingredients))])
    durability = sum([ingredients[i].durability * number_of_ingredients[i] for i in range(len(ingredients))])
    flavor = sum([ingredients[i].flavor * number_of_ingredients[i] for i in range(len(ingredients))])
    texture = sum([ingredients[i].texture * number_of_ingredients[i] for i in range(len(ingredients))])

    if any(part <= 0 for part in[capacity, durability, flavor, texture]):
        return 0

    return capacity * durability * flavor * texture


def d15p1(data):
    """
    Today, you set out on the task of perfecting your milk-dunking cookie recipe.
    All you have to do is find the right balance of ingredients.
    Your recipe leaves room for exactly 100 teaspoons of ingredients.
    You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input)
    and their properties per teaspoon:
        capacity (how well it helps the cookie absorb milk)
        durability (how well it keeps the cookie intact when full of milk)
        flavor (how tasty it makes the cookie)
        texture (how it improves the feel of the cookie)
        calories (how many calories it adds to the cookie)
    You can only measure ingredients in whole-teaspoon amounts accurately,
    and you have to be accurate so you can reproduce your results in the future.
    The total score of a cookie can be found by adding up each of the properties
    (negative totals become 0) and then multiplying together everything except calories.

    For instance, suppose you have these two ingredients:
        Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
    Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon
    (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:
        A capacity of 44*-1 + 56*2 = 68
        A durability of 44*-2 + 56*3 = 80
        A flavor of 44*6 + 56*-2 = 152
        A texture of 44*3 + 56*-1 = 76
    Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now)
    results in a total score of 62842880, which happens to be the best score possible given these ingredients.
    If any properties had produced a negative total, it would have instead become zero,
    causing the whole score to multiply to zero.

    Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
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
    Your cookie recipe becomes wildly popular!
    Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement).
    Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).
    For example, given the ingredients above,
        if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100),
        the total calorie count would be 40*8 + 60*3 = 500.
        The total score would go down, though: only 57600000, the best you can do in such trying circumstances.
    Given the ingredients in your kitchen and their properties,
    what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
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
