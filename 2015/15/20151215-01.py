import re
import sys
from typing import Iterator, Tuple

qualities = "capacity durability flavor texture".split()


def generate_all_tuples(n: int, desired_sum: int) -> Iterator[Tuple[int]]:
    if n <= 0:
        return
    if n == 1:
        yield (desired_sum,)
    for i in range(desired_sum + 1):
        for t in generate_all_tuples(n - 1, desired_sum - i):
            yield (i,) + t


def cookie_score(ings: dict, amounts: Tuple[int]) -> int:
    score = 1
    for q in qualities:
        this_quality = 0
        for i, a in enumerate(amounts):
            this_quality += a * ings[i][q]
        score *= max(this_quality, 0)
    return score


pattern = re.compile(r"(\S+) (-?\d+)")

ingredients = []

with open(sys.argv[1], "r") as file:
    for line in file:
        ingredient = {}
        for k, v in re.findall(pattern, line):
            ingredient[k] = int(v)
        ingredients.append(ingredient)

best_score = 0
for t in generate_all_tuples(len(ingredients), 100):
    best_score = max(best_score, cookie_score(ingredients, t))

print(best_score)
