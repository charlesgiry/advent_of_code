"""
aoc y2015 day 20
https://adventofcode.com/2015/day/20
"""
from itertools import combinations
from copy import deepcopy


class Item:
    """

    """
    name: str
    attack: int
    defence: int
    price: int

    def __init__(self, name, price, attack, defence):
        """

        """
        self.name = name
        self.price = price
        self.attack = attack
        self.defence = defence

    def __repr__(self):
        """

        """
        return self.name


class Character:
    """

    """
    name: str
    hp: int
    damage: int
    defence: int
    price: int
    inventory: list[Item]

    def __init__(self, name) -> None:
        """

        """
        self.name = name
        self.hp = 100
        self.damage = 0
        self.defence = 0
        self.price = 0
        self.inventory = []

    def equips(self, item: Item):
        """

        """
        self.inventory.append(item)
        self.damage += item.attack
        self.defence += item.defence
        self.price += item.price

    def unequips(self, item: Item):
        """

        """
        self.damage -= item.attack
        self.defence -= item.defence
        self.price -= item.price
        self.inventory.remove(item)

    def attack(self, other_character: 'Character', print_=False) -> None:
        """

        """
        current_attack = self.damage - other_character.defence
        current_attack = 1 if current_attack <= 1 else current_attack
        other_character.hp -= current_attack
        other_character.hp = 0 if other_character.hp <= 0 else other_character.hp
        if print_:
            print(f'{self.name} attacks {other_character.name}. it deals {current_attack} damage. {other_character.name} has {other_character.hp} hp left.')

    def __repr__(self):
        """

        """
        return f'{self.name}, hp: {self.hp}, damage: {self.damage}, def: {self.defence}, inventory: {self.inventory}, price: {self.price}'

    def __lt__(self, other):
        """

        """
        return self.price < other.price


def vs(c1, c2, print_=False):
    """

    """
    while c1.hp > 0 and c2.hp > 0:
        c1.attack(c2)
        if c2.hp > 0:
            c2.attack(c1)
    loser = c1 if c1.hp == 0 else c2
    if print_:
        print(f'{loser.name} dies')
    return loser


def d21parse(data):
    """

    """
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
    part 1
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
    part 2
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
