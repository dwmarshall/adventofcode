import re
import sys

registers = {}
output = []
IP = 0


def dv(exponent: int) -> int:
    return registers["A"] // (2**exponent)


def value(combo: int) -> int:
    match combo:
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case _:
            return combo


with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"Register ([A-C]): (\d+)", line):
            registers[m.group(1)] = int(m.group(2))
        if m := re.match(r"Program: (\S+)", line):
            program = list(map(int, m.group(1).split(",")))

while IP < len(program):
    opcode, operand = program[IP : IP + 2]
    IP += 2
    match opcode:
        case 0:
            registers["A"] = dv(value(operand))
        case 1:
            registers["B"] ^= operand
        case 2:
            registers["B"] = value(operand) & 7
        case 3:
            if registers["A"] != 0:
                IP = operand
        case 4:
            registers["B"] = registers["B"] ^ registers["C"]
        case 5:
            output.append(str(value(operand) & 7))
        case 6:
            registers["B"] = dv(value(operand))
        case 7:
            registers["C"] = dv(value(operand))


print(f"Output is {",".join(output)}")
