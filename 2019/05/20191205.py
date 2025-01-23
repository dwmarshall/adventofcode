from collections.abc import Iterator
import sys

OPERANDS = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}


def run(p: list[int], input: int) -> Iterator[int]:

    p = p[:]
    IP = 0
    while IP < len(p):
        instruction = p[IP] % 100
        opcode = f"{p[IP]:05}"
        operands = []
        for i in range(1, 1 + OPERANDS[instruction]):
            if IP + i < len(p):
                value = p[IP + i] if opcode[3 - i] == "1" else p[p[IP + i]]
                operands.append(value)
        match instruction:
            case 1:
                p[p[IP + 3]] = operands[0] + operands[1]
                IP += 4
            case 2:
                p[p[IP + 3]] = operands[0] * operands[1]
                IP += 4
            case 3:
                p[p[IP + 1]] = input
                IP += 2
            case 4:
                yield operands[0]
                IP += 2
            case 5:
                if operands[0] != 0:
                    IP = operands[1]
                else:
                    IP += 3
            case 6:
                if operands[0] == 0:
                    IP = operands[1]
                else:
                    IP += 3
            case 7:
                p[p[IP + 3]] = 1 if operands[0] < operands[1] else 0
                IP += 4
            case 8:
                p[p[IP + 3]] = 1 if operands[0] == operands[1] else 0
                IP += 4
            case 99:
                break


with open(sys.argv[1], "r") as file:
    program = list(map(int, file.readline().split(",")))

# Part 1
for x in run(program, 1):
    if x != 0:
        print(f"Part 1: output is {x}")

# Part 2

for x in run(program, 5):
    print(f"Part 2: The code is {x}")
