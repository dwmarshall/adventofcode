import sys


def accumulator(p: list[list[list[str]]], terminal_mode: bool = False) -> int:
    IP = 0
    acc = 0
    executed = set()

    while IP < len(p):
        if IP in executed:
            return None if terminal_mode else acc
        executed.add(IP)
        match p[IP]:
            case ["nop", value]:
                IP += 1
            case ["acc", value]:
                acc += int(value)
                IP += 1
            case ["jmp", value]:
                IP += int(value)
    return acc


with open(sys.argv[1], "r") as file:
    program = [x.strip().split() for x in file.readlines()]


print(f"Part 1: The accumulator is {accumulator(program)}")

# Part 2
swaps = [i for i, instruction in enumerate(program) if instruction[0] in {"jmp", "nop"}]

for line_number in swaps:
    instruction = program[line_number][0]
    program[line_number][0] = "jmp" if instruction == "nop" else "nop"
    if (a := accumulator(program, True)) is not None:
        print(f"Part 2: The accumulator is {a}")
        break
    program[line_number][0] = instruction
