import sys

with open(sys.argv[1], "r") as file:
    program = list(map(int, file.readlines()))

p1_program = program.copy()
p1_steps = 0
IP = 0

while 0 <= IP < len(p1_program):
    p1_program[IP] += 1
    IP += p1_program[IP] - 1
    p1_steps += 1

print(f"Part 1: we exited in {p1_steps} steps")

p2_program = program.copy()
p2_steps = 0
IP = 0

while 0 <= IP < len(p2_program):
    new_IP = IP + p2_program[IP]
    if p2_program[IP] >= 3:
        p2_program[IP] -= 1
    else:
        p2_program[IP] += 1
    IP = new_IP
    p2_steps += 1

print(f"Part 2: We exited in {p2_steps} steps")
