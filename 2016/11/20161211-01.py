from collections.abc import Iterator
import copy
from itertools import combinations, product

# test data
# each floor is a list The first item is a set of microchips,
# and the second item is a set of generators.
floors = [
    [{"H", "L"}, set()],
    [set(), {"H"}],
    [set(), {"L"}],
    [set(), set()],
]
# real data

floors = [
    [{"Pr"}, {"Pr"}],
    [set(), {"Co", "Cu", "Ru", "Pu"}],
    [{"Co", "Cu", "Ru", "Pu"}, set()],
    [set(), set()],
]

# part two
# floors = [
#     [{"Di", "El", "Pr"}, {"Di", "El", "Pr"}],
#     [set(), {"Co", "Cu", "Ru", "Pu"}],
#     [{"Co", "Cu", "Ru", "Pu"}, set()],
#     [set(), set()],
# ]


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
    for m, g in product(M, G):
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
        state_hash = hash((elevator, freeze(f)))
        if state_hash in seen:
            continue
        seen.add(state_hash)
        if finished(f):
            winning_steps = step - 1
            break
        for M, G in choices(f[elevator]):
            if elevator > 0:
                going_down = copy.deepcopy(f)
                going_down[elevator][0] -= M
                going_down[elevator - 1][0] |= M
                going_down[elevator][1] -= G
                going_down[elevator - 1][1] |= G
                new_hash = hash((elevator - 1, freeze(going_down)))
                if valid(going_down) and new_hash not in seen:
                    new_states.append((elevator - 1, going_down))
            if elevator + 1 < len(f):
                going_up = copy.deepcopy(f)
                going_up[elevator][0] -= M
                going_up[elevator + 1][0] |= M
                going_up[elevator][1] -= G
                going_up[elevator + 1][1] |= G
                new_hash = hash((elevator + 1, freeze(going_up)))
                if valid(going_up) and new_hash not in seen:
                    new_states.append((elevator + 1, going_up))
    states = new_states

print(f"Completed after {winning_steps} steps")
