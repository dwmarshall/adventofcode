from collections.abc import Iterator
import copy
from itertools import combinations, product
import re
import sys

element_map = {
    "cobalt": "Co",
    "curium": "Cu",
    "hydrogen": "H",
    "lithium": "L",
    "plutonium": "Pu",
    "promethium": "Pr",
    "ruthenium": "Ru",
}

floors = [lambda: [set(), set()] for _ in range(4)]
print(floors)

with open(sys.argv[1], "r") as file:
    for i, line in enumerate(file):
        new_floor = [set(), set()]
        for microchip in re.findall(r"(\S+)-compatible microchip", line):
            new_floor[0].add(element_map[microchip])
        for generator in re.findall(r"(\S+) generator", line):
            new_floor[1].add(element_map[generator])
        floors[i] = new_floor


if len(sys.argv) > 2 and sys.argv[2] == "--hard":
    for i in range(2):
        for x in ["Di", "El"]:
            floors[0][i].add(x)


def freeze(f: list[list[set]]) -> tuple[tuple[frozenset]]:
    frozen_list = []
    for floor in f:
        t = tuple(map(frozenset, floor))
        frozen_list.append(t)
    return tuple(frozen_list)


def choices(f: list[list[set]]) -> Iterator[tuple[set]]:
    """yields a tuple of two sets"""
    f = copy.deepcopy(f)
    M, G = f
    # first, yield all the tuples of exactly one item
    for m in M:
        yield ({m}, set())
    for g in G:
        yield (set(), {g})
    # yield the combinations of two of each kind
    for m in combinations(M, 2):
        yield (set(m), set())
    for g in combinations(G, 2):
        yield (set(), set(g))
    # finally, yield the combinations
    pair_found = False
    for m, g in product(M, G):
        if m == g:
            if pair_found:
                continue
            else:
                pair_found = True
        yield ({m}, {g})


def valid(f: list[list[set]]) -> bool:
    for floor in f:
        M, G = floor
        paired = M & G
        if (M - paired) and G:
            return False
    return True


def finished(f: list[list[set]]) -> bool:
    return not any(g[0] or g[1] for g in f[:-1])


def items_below(f: list[list[set]], e: int) -> bool:
    for floor in f[0 : e + 1]:
        if floor[0] or floor[1]:
            return True
    return False


initial_state = (0, floors)
states = [initial_state]
step = 0
seen = set()
winning_steps = None

while winning_steps is None:
    step += 1
    print(f"Starting step {step} with {len(states)} states")
    new_states = []
    for s in states:
        elevator, f = s
        if finished(f):
            winning_steps = step - 1
            break
        # going up
        if elevator > 0 and items_below(f, elevator):
            for M, G in choices(f[elevator]):
                going_down = copy.deepcopy(f)
                going_down[elevator][0] -= M
                going_down[elevator - 1][0] |= M
                going_down[elevator][1] -= G
                going_down[elevator - 1][1] |= G
                new_hash = hash((elevator - 1, freeze(going_down)))
                if valid(going_down) and new_hash not in seen:
                    new_states.append((elevator - 1, going_down))
                    seen.add(new_hash)
        if elevator + 1 < len(f):
            for M, G in choices(f[elevator]):
                going_up = copy.deepcopy(f)
                going_up[elevator][0] -= M
                going_up[elevator + 1][0] |= M
                going_up[elevator][1] -= G
                going_up[elevator + 1][1] |= G
                new_hash = hash((elevator + 1, freeze(going_up)))
                if valid(going_up) and new_hash not in seen:
                    new_states.append((elevator + 1, going_up))
                    seen.add(new_hash)
    states = new_states

print(f"Completed after {winning_steps} steps")
