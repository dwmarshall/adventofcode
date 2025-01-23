import sys

orbits = dict()


def number_of_orbits(s: str) -> int:
    if s == "COM":
        return 0
    return 1 + number_of_orbits(orbits[s])


with open(sys.argv[1], "r") as file:
    for line in file:
        orbited, orbiting = line.strip().split(")")
        orbits[orbiting] = orbited

p1_orbits = sum(number_of_orbits(x) for x in orbits.keys())
print(f"Part 1: Total orbits are {p1_orbits}")

# Part 2

# What is Santa's path to COM?
santa_path = []
curr = "SAN"
while curr != "COM":
    curr = orbits[curr]
    santa_path.append(curr)

# What is my path?
curr = orbits["YOU"]
transfers = 0
while curr not in santa_path:
    transfers += 1
    curr = orbits[curr]


print(f"Part 2: There are {transfers + santa_path.index(curr)} transfers")
