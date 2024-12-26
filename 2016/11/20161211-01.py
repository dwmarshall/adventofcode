from collections.abc import Iterator
import copy
import heapq
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


def freeze(f: list[list[set]]) -> tuple[tuple[frozenset]]:
    frozen_list = []
    for floor in f:
        t = tuple(map(frozenset, floor))
        frozen_list.append(t)
    return tuple(frozen_list)


def thaw(f: tuple[tuple[frozenset]]) -> list[list[set]]:
    thawed_list = []
    for floor in f:
        thawed = list(map(set, floor))
        thawed_list.append(thawed)
    return thawed_list


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


def invalid(f: list[list[set]]) -> bool:
    for g in f:
        M, G = g
        ignore = M & G
        microchips = M - ignore
        generators = G - ignore
        if microchips and generators:
            return True
    return False


def finished(f: list[list[set]]) -> bool:
    return not any(g[0] or g[1] for g in f[:-1])


# initial state, elevator on floor 0
q = [(0, 0, floors)]

seen = set()

while q:
    steps, elevator, f = heapq.heappop(q)
    if (elevator, freeze(f)) in seen:
        continue
    seen.add((elevator, freeze(f)))
    print(steps, elevator, f)
    if invalid(f):
        continue
    if finished(f):
        print(f"Completed after {steps} steps")
        break
    for M, G in choices(f[elevator]):
        if elevator > 0:
            going_down = copy.deepcopy(f)
            going_down[elevator][0] -= M
            going_down[elevator - 1][0] |= M
            going_down[elevator][1] -= G
            going_down[elevator - 1][1] |= G
            heapq.heappush(q, (steps + 1, elevator - 1, going_down))
        if elevator + 1 < len(f):
            going_up = copy.deepcopy(f)
            going_up[elevator][0] -= M
            going_up[elevator + 1][0] |= M
            going_up[elevator][1] -= G
            going_up[elevator + 1][1] |= G
            heapq.heappush(q, (steps + 1, elevator + 1, going_up))
