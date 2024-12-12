import re
import sys

reindeer = re.compile(
    r"(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)"
)

TICKS = int(sys.argv[1])
winning_distance = 0


def distance(speed: int, duration: int, rest: int) -> int:
    t = TICKS
    d = 0
    while t > 0:
        if t <= duration:
            d += speed * t
            t = 0
        else:
            d += speed * duration
            t -= duration
        t -= rest
    return d


with open(sys.argv[2], "r") as file:
    for line in file:
        m = reindeer.match(line)
        name, s, d, r = m.groups()
        s = int(s)
        d = int(d)
        r = int(r)
        winning_distance = max(winning_distance, distance(s, d, r))

print(winning_distance)
