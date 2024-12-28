import re
import sys

with open(sys.argv[1], "r") as file:
    program = file.readlines()


def run(p: list[str], a: int, b: int) -> dict[str, int]:
    IP = 0

    registers = {"a": a, "b": b}

    while IP < len(p):
        if m := re.match(r"(hlf|tpl|inc) (a|b)", p[IP]):
            IP += 1
            opcode, reg = m.groups()
            match opcode:
                case "hlf":
                    registers[reg] //= 2
                case "tpl":
                    registers[reg] *= 3
                case "inc":
                    registers[reg] += 1
        elif m := re.match(r"jmp ([\+\-]\d+)", p[IP]):
            IP += int(m.group(1))
        elif m := re.match(r"(jie|jio) (a|b), ([\+\-]\d+)", p[IP]):
            opcode, reg, offset = m.groups()
            offset = int(offset)
            match opcode:
                case "jie":
                    IP += offset if registers[reg] % 2 == 0 else 1
                case "jio":
                    IP += offset if registers[reg] == 1 else 1

    return registers


print(f"Part 1: {run(program, 0, 0)}")
print(f"Part 2: {run(program, 1, 0)}")
