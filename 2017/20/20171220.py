from collections import Counter, deque
import copy
import re
import sys


class Particle:
    def __init__(
        self, p: tuple[int, int, int], v: tuple[int, int, int], a: tuple[int, int, int]
    ):

        self.position = p
        self.velocity = v
        self.acceleration = a

    def distance(self) -> int:
        return sum(abs(x) for x in self.position)

    def tick(self) -> None:
        self.velocity = tuple(a + b for a, b in zip(self.velocity, self.acceleration))
        self.position = tuple(a + b for a, b in zip(self.position, self.velocity))


particles = []

tuple_pattern = r"<(-?\d+),(-?\d+),(-?\d+)>"

with open(sys.argv[1], "r") as file:
    for line in file:
        parameters = []
        for t in re.findall(tuple_pattern, line):
            parameters.append(tuple(int(x) for x in t))
        particles.append(Particle(*parameters))

# Part 1

p1_particles = copy.deepcopy(particles)
P1_THRESHOLD = 1000

p1_winner = deque([], P1_THRESHOLD)

while len(p1_winner) < P1_THRESHOLD or len(set(p1_winner)) > 1:
    closest_distance = float("inf")
    closest_particle = None
    for i, p in enumerate(p1_particles):
        p.tick()
        if (d := p.distance()) < closest_distance:
            closest_distance = d
            closest_particle = i
    p1_winner.append(closest_particle)

print(f"Part 1: The winning particle is {p1_winner[0]}")

p2_particles = copy.deepcopy(particles)
P2_THRESHOLD = 1000

p2_winner = deque([], P2_THRESHOLD)

while len(p2_winner) < P2_THRESHOLD or len(set(p2_winner)) > 1:
    p2_positions = Counter()
    for p in p2_particles:
        if p is not None:
            p.tick()
            p2_positions[p.position] += 1
    for i, p in enumerate(p2_particles):
        if p is not None and p2_positions[p.position] > 1:
            particles[i] = None
    remaining_particles = sum(0 if p is None else 1 for p in particles)
    p2_winner.append(remaining_particles)

print(f"Part 2: There are {p2_winner[0]} particles remaining")
