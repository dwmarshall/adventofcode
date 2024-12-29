import re
import sys

with open(sys.argv[1], "r") as file:
    program = file.readlines()


def run(p: list[str], r: list[int] = [0, 0, 0, 0]) -> dict[str, int]:
    IP = 0

    registers = dict(zip("abcd", r))

    while IP < len(p):
        if m := re.match(r"cpy ([a-d]|\d+) ([a-d])", p[IP]):
            IP += 1
            src, dest = m.groups()
            if src in "abcd":
                registers[dest] = registers[src]
            else:
                registers[dest] = int(src)
        elif m := re.match(r"(inc|dec) ([abcd])", p[IP]):
            IP += 1
            op, r = m.groups()
            if op == "inc":
                registers[r] += 1
            else:
                registers[r] -= 1
        elif m := re.match(r"jnz (\d+|[abcd]) (-?\d+)", p[IP]):
            r, dest = m.groups()
            value = registers[r] if r in "abcd" else int(r)
            IP += int(dest) if value != 0 else 1

    return registers


print(f"Part 1: {run(program)}")
print(f"Part 2: {run(program, [0, 0, 1, 0])}")
