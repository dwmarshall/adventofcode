import copy
import sys

program = []

with open(sys.argv[1], "r") as file:
    for line in file:
        loc = line.strip().split()
        for i in range(1, len(loc)):
            if loc[i] not in "abcd":
                loc[i] = int(loc[i])
        program.append(loc)


def toggle(op: list[str | int]) -> list[str | int]:
    if len(op) == 2:
        op[0] = "dec" if op[0] == "inc" else "inc"
    if len(op) == 3:
        op[0] = "cpy" if op[0] == "jnz" else "jnz"
    return op


def run(p: list[str], r: list[int] = [0, 0, 0, 0]) -> dict[str, int]:
    IP = 0

    registers = dict(zip("abcd", r))
    p = copy.deepcopy(p)

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
            case "tgl", t:
                t = registers[t] if str(t) in "abcd" else t
                if 0 <= IP + t < len(program):
                    p[IP + t] = toggle(p[IP + t])
                IP += 1
            case _:
                print(f"No match for {p[IP]}")
                IP += 1
    return registers


print(f"Part 1: {run(program, [7, 0, 0, 0])}")
print(f"Part 2: {run(program, [12, 0, 0, 0])}")
