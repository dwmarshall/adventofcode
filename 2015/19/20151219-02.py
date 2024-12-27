import random
import re
import sys

element = r"(?:[A-Z][a-z]?)"
diatom = rf"{element}{element}"
complex = rf"{element}Rn{element}(?:Y{element})*Ar"

atom_map = dict()
complex_map = dict()
final_set = set()

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(rf"(e|{element}) => ({element}+)\s*$", line.strip()):
            el, mol = m.groups()
            atom_map[mol] = el
        elif line != "\n":
            molecule = line.strip()


def backtrack(s: str) -> int:
    steps = 0
    old_s = ""
    atom_keys = list(atom_map.keys())
    random.shuffle(atom_keys)
    while s != old_s:
        old_s = s
        for k in atom_keys:
            while k in s:
                steps += s.count(k)
                s = s.replace(k, atom_map[k])
    return steps if s == "e" else 0


total_steps = 0

while total_steps == 0:
    total_steps = backtrack(molecule)

print(f"Total steps is {total_steps}")
