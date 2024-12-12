import re
import sys
from typing import Iterator

reindeer = re.compile(
    r"(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)"
)

TICKS = int(sys.argv[1])

racers = []


def reindeer_generator(speed: int, duration: int, rest: int) -> Iterator[int]:
    d = 0
    t = 0
    cycle = duration + rest
    while True:
        if t % cycle < duration:
            d += speed
        yield d
        t += 1


with open(sys.argv[2], "r") as file:
    for line in file:
        m = reindeer.match(line)
        name, s, d, r = m.groups()
        s = int(s)
        d = int(d)
        r = int(r)
        racers.append(reindeer_generator(s, d, r))

distances = [0] * len(racers)
points = [0] * len(racers)

for t in range(1, TICKS + 1):
    for i in range(len(racers)):
        distances[i] = next(racers[i])
        leader = max(distances)
    point_index = distances.index(leader)
    points[point_index] += 1

print(max(points))
