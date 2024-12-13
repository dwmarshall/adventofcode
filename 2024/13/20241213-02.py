import re
import sys
from typing import List, Tuple


def cramer(c: List[List[int]], a: List[int]) -> Tuple[int]:
    # Assumes a 2x2 matrix
    det = c[0][0] * c[1][1] - c[0][1] * c[1][0]
    detA = c[0][0] * a[1] - c[1][0] * a[0]
    detB = a[0] * c[1][1] - c[0][1] * a[1]
    A = detB // det
    B = detA // det
    if A * c[0][0] + B * c[0][1] == a[0] and A * c[1][0] + B * c[1][1] == a[1]:
        return (A, B)
    else:
        return None


machines = []
with open(sys.argv[1], "r") as file:
    machine = {}
    for line in file:
        if m := re.match(r"Button ([AB])", line):
            button = m.group(1)
            xy = re.search(r"X\+(\d+), Y\+(\d+)", line)
            machine[button] = {"X": int(xy.group(1)), "Y": int(xy.group(2))}
        elif line.startswith("Prize"):
            prize = re.search(r"X=(\d+), Y=(\d+)", line)
            machine["P"] = {"X": int(prize.group(1)), "Y": int(prize.group(2))}
            machines.append(machine)
            machine = {}

total_cost = 0

for m in machines:
    x_row = [m["A"]["X"], m["B"]["X"]]
    y_row = [m["A"]["Y"], m["B"]["Y"]]
    coefficients = [x_row, y_row]
    constants = [m["P"]["X"] + int(1e13), m["P"]["Y"] + int(1e13)]
    if t := cramer(coefficients, constants):
        A, B = t
        total_cost += 3 * A + B
print(total_cost)
