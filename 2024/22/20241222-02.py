from collections import Counter
from itertools import islice, pairwise
import operator
import sys
from typing import Iterator

mix = operator.__xor__


def prune(x: int) -> int:
    return x % 16777216


def sn_generator(n: int) -> Iterator[int]:
    while True:
        yield n
        n = prune(mix(n, 64 * n))
        n = prune(mix(n, n // 32))
        n = prune(mix(n, n * 2048))


all_series = []
all_tuples = set()

with open(sys.argv[1], "r") as file:
    for line in file:
        v = int(line.strip())
        numbers = list(islice(sn_generator(v), 2001))
        bananas = [x % 10 for x in numbers]
        changes = [b - a for a, b in pairwise(bananas)]
        series = Counter()

        for i in range(len(numbers) - 4):
            t = tuple(changes[i : i + 4])
            if t not in series:
                series[t] = bananas[i + 4]
            all_tuples.add(t)
        all_series.append(series)

all_bananas = Counter()
for each_series in all_tuples:
    all_bananas[each_series] = sum(s[each_series] for s in all_series)


print(all_bananas.most_common(1)[0])
print(max(all_bananas.values()))
