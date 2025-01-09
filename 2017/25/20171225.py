from collections import defaultdict
import re
import sys

program = {}
tape = defaultdict(int)
position = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"Begin in state ([A-Z])", line):
            state = m.group(1)
        elif m := re.search(r"checksum after (\d+)", line):
            checksum_count = int(m.group(1))
        elif m := re.match(r"In state ([A-Z])", line):
            current_program = m.group(1)
            program[current_program] = {}
        elif m := re.search(r"current value is ([01])", line):
            current_value = int(m.group(1))
            program[current_program][current_value] = {}
        elif m := re.search(r"Write the value ([01])", line):
            program[current_program][current_value]["write"] = int(m.group(1))
        elif m := re.search(r"Move one slot to the (left|right)", line):
            program[current_program][current_value]["move"] = m.group(1)
        elif m := re.search(r"Continue with state ([A-Z])", line):
            program[current_program][current_value]["state"] = m.group(1)


while checksum_count > 0:
    instruction = program[state][tape[position]]
    tape[position] = instruction["write"]
    position += 1 if instruction["move"] == "right" else -1
    state = instruction["state"]
    checksum_count -= 1

print(f"The checksum is {sum(tape.values())}")
