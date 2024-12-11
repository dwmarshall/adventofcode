from functools import cache
import sys
from typing import List

BLINKS = 75
total_stones = 0


@cache
def stones(stone: int, blinks: int = BLINKS) -> int:
    if blinks == 0:
        return 1
    new_stones = blink(stone)
    total = 0
    for s in new_stones:
        total += stones(s, blinks - 1)
    return total


@cache
def blink(stone: int) -> List[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        t = str(stone)
        return [int(t[: len(t) // 2]), int(t[len(t) // 2 :])]
    else:
        return [stone * 2024]


with open(sys.argv[1], "r") as file:
    line = file.read()
    original_stones = list(map(int, line.strip().split()))

for each_stone in original_stones:
    total_stones += stones(each_stone)

print(total_stones)

# Display cache statistics
info = stones.cache_info()
hit_rate = (
    (info.hits / (info.hits + info.misses)) * 100
    if (info.hits + info.misses) > 0
    else 0
)
print(f"Cache hits: {info.hits}")
print(f"Cache misses: {info.misses}")
print(f"Hit rate: {hit_rate:.2f}%")

info = blink.cache_info()
hit_rate = (
    (info.hits / (info.hits + info.misses)) * 100
    if (info.hits + info.misses) > 0
    else 0
)
print(f"Cache hits: {info.hits}")
print(f"Cache misses: {info.misses}")
print(f"Hit rate: {hit_rate:.2f}%")
