import heapq
from itertools import pairwise, product
import math
import sys


def keypad_paths(keypad: dict[str, str]) -> dict[str, str]:

    paths = {x: {y: set() for y in keypad} for x in keypad}

    for k1, v1 in keypad.items():
        paths[k1][k1].add("")
        for k2, v2 in v1.items():
            paths[k1][k2].add(v2)

    for k1 in keypad:
        q = []
        for k2 in keypad:
            distance = math.inf if paths[k1][k2] is None else len(paths[k1][k2])
            heapq.heappush(q, (distance, k2))
        unvisited = set(keypad)
        while q:
            _, k2 = heapq.heappop(q)
            if k2 not in unvisited:
                continue
            if len(paths[k1][k2]) == 0:
                continue
            unvisited.remove(k2)
            for k3 in unvisited:
                if len(paths[k2][k3]) == 0:
                    continue
                for k1k2, k2k3 in product(paths[k1][k2], paths[k2][k3]):
                    new_path = k1k2 + k2k3
                    if len(paths[k1][k3]) == 0 or len(new_path) == min(
                        map(len, paths[k1][k3])
                    ):
                        paths[k1][k3].add(new_path)
                    elif len(new_path) < min(map(len, paths[k1][k3])):
                        paths[k1][k3] = {new_path}
                    heapq.heappush(q, (len(new_path), k3))
    return paths


def presses(code: str, keymap: dict[str, str]) -> set[str]:
    keys = []
    for k1, k2 in pairwise(["A"] + list(code)):
        this_key = []
        for s in keymap[k1][k2]:
            this_key.append(s)
        keys.append(this_key)
    # print(keys)
    results = []
    for t in product(*keys):
        results.append("A".join(t) + "A")
    return results


first_keypad = {
    "A": {"0": "<", "3": "^"},
    "0": {"A": ">", "2": "^"},
    "1": {"2": ">", "4": "^"},
    "2": {"0": "v", "1": "<", "3": ">", "5": "^"},
    "3": {"A": "v", "2": "<", "6": "^"},
    "4": {"1": "v", "5": ">", "7": "^"},
    "5": {"2": "v", "4": "<", "6": ">", "8": "^"},
    "6": {"3": "v", "5": "<", "9": "^"},
    "7": {"4": "v", "8": ">"},
    "8": {"5": "v", "7": "<", "9": ">"},
    "9": {"6": "v", "8": "<"},
}

first_map = keypad_paths(first_keypad)

second_keypad = {
    "^": {"A": ">", "v": "v"},
    "A": {"^": "<", ">": "v"},
    "<": {"v": ">"},
    "v": {"<": "<", "^": "^", ">": ">"},
    ">": {"v": "<", "A": "^"},
}

second_map = keypad_paths(second_keypad)

input = []

with open(sys.argv[1], "r") as file:
    for line in file:
        input.append(line.strip())

complexity = 0

for x in input:
    value = int(x.lstrip("0").rstrip("A"))
    first_seq = presses(x, first_map)
    first_min = min(map(len, first_seq))
    second_seq = []
    for fs in [x for x in first_seq if len(x) == first_min]:
        second_seq.extend(presses(fs, second_map))
    second_min = min(map(len, second_seq))
    third_seq = []
    for ss in [x for x in second_seq if len(x) == second_min]:
        third_seq.extend(presses(ss, second_map))
    multiplier = min(map(len, third_seq))
    complexity += value * multiplier

print(f"Final complexity is {complexity}")
