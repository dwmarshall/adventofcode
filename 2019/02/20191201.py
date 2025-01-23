import sys


def run(p: list[int], noun: int, verb: int) -> int:

    p = p[:]
    p[1] = noun
    p[2] = verb
    IP = 0
    while IP < len(p):
        match p[IP]:
            case 1:
                p[p[IP + 3]] = p[p[IP + 1]] + p[p[IP + 2]]
            case 2:
                p[p[IP + 3]] = p[p[IP + 1]] * p[p[IP + 2]]
            case 99:
                return p[0]
        IP += 4


with open(sys.argv[1], "r") as file:
    program = list(map(int, file.readline().split(",")))

print(f"Part 1: Position 0 is {run(program, 12, 2)}")

GOAL = 19690720
noun = 0
while True:
    noun += 1
    result = run(program, noun, 0)
    if result > GOAL:
        noun -= 1
        break

verb = GOAL - run(program, noun, 0)
assert run(program, noun, verb) == GOAL

print(f"Part 2: The result is {100 * noun + verb}")
