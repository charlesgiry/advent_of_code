"""
aoc y2015 day 20
https://adventofcode.com/2015/day/20
"""
from itertools import combinations
from copy import deepcopy


class Item:
    name: str
    attack: int
    defence: int
    price: int

    def __init__(self, name, price, attack, defence):
        self.name = name
        self.price = price
        self.attack = attack
        self.defence = defence

    def __repr__(self):
        return self.name


class Character:
    name: str
    hp: int
    damage: int
    defence: int
    price: int
    inventory: list[Item]

    def __init__(self, name) -> None:
        self.name = name
        self.hp = 100
        self.damage = 0
        self.defence = 0
        self.price = 0
        self.inventory = []

    def equips(self, item: Item):
        self.inventory.append(item)
        self.damage += item.attack
        self.defence += item.defence
        self.price += item.price

    def unequips(self, item: Item):
        self.damage -= item.attack
        self.defence -= item.defence
        self.price -= item.price
        self.inventory.remove(item)

    def attack(self, other_character: 'Character', print_=False) -> None:
        current_attack = self.damage - other_character.defence
        current_attack = 1 if current_attack <= 1 else current_attack
        other_character.hp -= current_attack
        other_character.hp = 0 if other_character.hp <= 0 else other_character.hp
        if print_:
            print(f'{self.name} attacks {other_character.name}. it deals {current_attack} damage. {other_character.name} has {other_character.hp} hp left.')

    def __repr__(self):
        return f'{self.name}, hp: {self.hp}, damage: {self.damage}, def: {self.defence}, inventory: {self.inventory}, price: {self.price}'

    def __lt__(self, other):
        return self.price < other.price


def vs(c1, c2, print_=False):
    while c1.hp > 0 and c2.hp > 0:
        c1.attack(c2)
        if c2.hp > 0:
            c2.attack(c1)
    loser = c1 if c1.hp == 0 else c2
    if print_:
        print(f'{loser.name} dies')
    return loser


def d21parse(data):
    boss = Character('Boss')
    boss_hp = int(data[0].split(': ')[1])
    boss_damage = int(data[1].split(': ')[1])
    boss_defence = int(data[2].split(': ')[1])

    boss.hp = boss_hp
    boss.damage = boss_damage
    boss.defence = boss_defence
    return boss


weapon_shop = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0)
]

armor_shop = [
    None,
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5)
]

accessory_shop = [
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3)
]
accessory_combination = []

for i in range(3):
    comb = combinations(accessory_shop, i)
    accessory_combination.extend(comb)


def d21p1(data: Character):
    """
    Little Henry Case got a new video game for Christmas.
    It's an RPG, and he's stuck on a boss.
    He needs to know what equipment to buy at the shop. He hands you the controller.

    In this game, the player (you) and the enemy (the boss) take turns attacking.
    The player always goes first. Each attack reduces the opponent's hit points by at least 1.
    The first character at or below 0 hit points loses.

    Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.
    An attacker always does at least 1 damage. So, if the attacker has a damage score of 8,
    and the defender has an armor score of 3, the defender loses 5 hit points.
    If the defender had an armor score of 300, the defender would still lose 1 hit point.

    Your damage score and armor score both start at zero.
    They can be increased by buying items in exchange for gold.
    You start with no items and have as much gold as you need.
    Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

    Here is what the item shop is selling:

    Weapons:    Cost  Damage  Armor
    Dagger        8     4       0
    Shortsword   10     5       0
    Warhammer    25     6       0
    Longsword    40     7       0
    Greataxe     74     8       0

    Armor:      Cost  Damage  Armor
    Leather      13     0       1
    Chainmail    31     0       2
    Splintmail   53     0       3
    Bandedmail   75     0       4
    Platemail   102     0       5

    Rings:      Cost  Damage  Armor
    Damage +1    25     1       0
    Damage +2    50     2       0
    Damage +3   100     3       0
    Defense +1   20     0       1
    Defense +2   40     0       2
    Defense +3   80     0       3

    You must buy exactly one weapon;
    no dual-wielding. Armor is optional, but you can't use more than one.
    You can buy 0-2 rings (at most one for each hand). You must use any items you buy.
    The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

    For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

    The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
    In this scenario, the player wins! (Barely.)

    You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?
    """
    wins = []
    for weapon in weapon_shop:
        player = Character('Player')
        boss = deepcopy(data)
        player.equips(weapon)

        for armor in armor_shop:
            if armor:
                player.equips(armor)

            for accessories in accessory_combination:
                for accessory in accessories:
                    player.equips(accessory)

                player.hp = 100
                boss.hp = data.hp
                loser = vs(player, boss)
                if loser == boss:
                    wins.append(deepcopy(player))

                for accessory in accessories:
                    player.unequips(accessory)

            if armor:
                player.unequips(armor)

    wins.sort()
    return wins[0].price


def d21p2(data):
    """
    Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants.
    The other rules still apply, and he still only has one of each item.
    What is the most amount of gold you can spend and still lose the fight?
    """
    loses = []
    for weapon in weapon_shop:
        player = Character('Player')
        boss = deepcopy(data)
        player.equips(weapon)

        for armor in armor_shop:
            if armor:
                player.equips(armor)

            for accessories in accessory_combination:
                for accessory in accessories:
                    player.equips(accessory)

                player.hp = 100
                boss.hp = data.hp
                loser = vs(player, boss)
                if loser == player:
                    loses.append(deepcopy(player))

                for accessory in accessories:
                    player.unequips(accessory)

            if armor:
                player.unequips(armor)

    loses.sort()
    return loses[-1].price
