from collections import deque
from collections.abc import Iterator
from hashlib import md5
from itertools import count, islice
import re
import sys

INPUT = sys.argv[1]
DEQUE_SIZE = 1001
KEYS_NEEDED = 64
STRETCHES = int(sys.argv[2]) if len(sys.argv) > 2 else 0


def keys(salt: str) -> Iterator[str]:
    for i in count(0):
        key = f"{salt}{i}"
        for _ in range(STRETCHES):
            key = md5(key.encode()).hexdigest()
        yield md5(key.encode()).hexdigest()


keystream = keys(INPUT)

keys_found = 0
last_key_index = None

d = deque(islice(keystream, DEQUE_SIZE), DEQUE_SIZE)
i = 0

while keys_found < KEYS_NEEDED:
    current_key = d[0]
    if m := re.search(r"(.)\1\1", current_key):
        letter = m.group(1)
        satisfying = [
            i + j for j, k in enumerate(islice(d, 1, None)) if letter * 5 in k
        ]
        if satisfying:
            keys_found += 1
            last_key_index = i
    d.append(next(keystream))
    i += 1

print(f"Last key index is {last_key_index}")
