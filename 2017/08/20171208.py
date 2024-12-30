from collections import defaultdict
import operator
import re
import sys

operators = r"(?:<=?)|(?:>=?)|(?:[=!]=)"
value = r"-?\d+"

comparisons = {
    ">": operator.__gt__,
    ">=": operator.__ge__,
    "<": operator.__lt__,
    "<=": operator.__le__,
    "==": operator.__eq__,
    "!=": operator.__ne__,
}

registers = defaultdict(int)
max_register = 0


def condition(reg: str, op: str, val: int) -> bool:
    return comparisons[op](registers[reg], val)


with open(sys.argv[1], "r") as file:
    for line in file:
        m = re.match(
            rf"(\S+) (inc|dec) ({value}) if (\S+) ({operators}) ({value})", line
        )
        tgt, opcode, val, left_reg, comparison, right_val = m.groups()
        val = int(val)
        right_val = int(right_val)
        if opcode == "dec":
            val = -val
        if condition(left_reg, comparison, right_val):
            registers[tgt] += val
            max_register = max(max_register, registers[tgt])

print(f"Part 1: The highest value in a register is {max(registers.values())}")
print(f"Part 2: The highest ever register content was {max_register}")
