import re
import sys
from typing import List

DEBUG = False

registers = {}
output = []
IP = 0


def program_output(new_A: int) -> List[int]:
    R = registers.copy()
    R["A"] = new_A

    IP = 0
    output = []
    while IP < len(program):
        opcode, literal = program[IP : IP + 2]
        match literal:
            case 4:
                combo = R["A"]
            case 5:
                combo = R["B"]
            case 6:
                combo = R["C"]
            case _:
                combo = literal
        IP += 2
        match opcode:
            case 0:
                R["A"] = R["A"] // (2**combo)
            case 1:
                R["B"] ^= literal
            case 2:
                R["B"] = combo % 8
            case 3:
                if R["A"] != 0:
                    IP = literal
            case 4:
                R["B"] = R["B"] ^ R["C"]
            case 5:
                output.append(combo % 8)
            case 6:
                R["B"] = R["A"] // (2**combo)
            case 7:
                R["C"] = R["A"] // (2**combo)
    return output


with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"Register ([A-C]): (\d+)", line):
            registers[m.group(1)] = int(m.group(2))
        if m := re.match(r"Program: (\S+)", line):
            program = list(map(int, m.group(1).split(",")))

candidates = [0]

for i in range(len(program) - 1, -1, -1):
    desired_output = program[i:]
    new_candidates = []
    for a in candidates:
        for k in range(8):
            this_output = program_output(a * 8 + k)
            if this_output == desired_output:
                new_candidates.append(a * 8 + k)
    candidates = new_candidates

print(min(candidates))
