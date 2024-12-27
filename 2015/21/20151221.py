import copy
from dataclasses import dataclass
from itertools import combinations, product
import sys


@dataclass
class Item:
    cost: int
    damage: int
    armor: int


@dataclass
class Fighter:
    hit_points: int
    damage: int
    armor: int


weapons = [
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(74, 8, 0),
]

armor = [
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5),
]

rings = [
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3),
]

kits = []

weapon_choices = [w for w in weapons]
armor_choices = [Item(0, 0, 0)] + [a for a in armor]
ring_choices = (
    [Item(0, 0, 0)]
    + [r for r in rings]
    + [
        Item(a.cost + b.cost, a.damage + b.damage, a.armor + b.armor)
        for a, b in combinations(rings, 2)
    ]
)

for t in product(weapon_choices, armor_choices, ring_choices):
    kit = Item(
        sum(i.cost for i in t),
        sum(i.damage for i in t),
        sum(i.armor for i in t),
    )
    kits.append(kit)


def player_wins(p: Fighter, k: Item, b: Fighter) -> bool:
    p = copy.deepcopy(p)
    b = copy.deepcopy(b)
    p.damage += k.damage
    p.armor += k.armor
    while b.hit_points > 0 and p.hit_points > 0:
        b.hit_points -= p.damage - b.armor
        p.hit_points -= b.damage - p.armor
    return b.hit_points <= 0


player = Fighter(100, 0, 0)
boss = Fighter(*list(map(int, sys.argv[1:4])))

winning_costs = []
losing_costs = []

for k in kits:
    if player_wins(player, k, boss):
        winning_costs.append(k.cost)
    else:
        losing_costs.append(k.cost)

print(f"Minimum winning cost is {min(winning_costs)}")
print(f"Maximum losing cost is {max(losing_costs)}")
