from collections.abc import Iterator
from itertools import count
import sys

program = []

TEST_VALUES = 100

with open(sys.argv[1], "r") as file:
    for line in file:
        loc = line.strip().split()
        for i in range(1, len(loc)):
            if loc[i] not in "abcd":
                loc[i] = int(loc[i])
        program.append(loc)


def run(p: list[str], A: int) -> Iterator[int]:
    IP = 0

    registers = dict(zip("bcd", [0] * 3))
    registers["a"] = A

    while IP < len(p):
        # print(f"IP = {IP}, instruction = {p[IP]}, registers = {registers}")
        match p[IP]:
            case "cpy", r1, r2:
                if str(r2) in "abcd":
                    registers[r2] = registers[r1] if str(r1) in "abcd" else r1
                IP += 1
            case "inc", r:
                registers[r] += 1
                IP += 1
            case "dec", r:
                registers[r] -= 1
                IP += 1
            case "jnz", r, offset:
                condition = registers[r] if str(r) in "abcd" else r
                dest = registers[offset] if str(offset) in "abcd" else offset
                IP += dest if condition != 0 else 1
            case "out", r:
                yield registers[r] if str(r) in "abcd" else r
                IP += 1
            case _:
                print(f"No match for {p[IP]}")
                IP += 1
    return registers


for a in count():
    output = run(program, a)
    passed = True
    for i in range(TEST_VALUES):
        if next(output) != i % 2:
            print(f"A = {a} failed at step {i}!")
            passed = False
            break
    if passed:
        print(f"Part 1: Minimum value for register a is {a}.")
        break
