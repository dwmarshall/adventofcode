from collections import defaultdict
import re
import sys

element_map = defaultdict(list)
result = set()

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"([A-Z][a-z]?) => (\S+)", line.strip()):
            element_map[m.group(1)].append(m.group(2))
        elif len(line.strip()) != 0:
            molecule = line.strip()

atoms = re.findall(r"[A-Z][a-z]?", molecule)

for i, atom in enumerate(atoms):
    for replacement in element_map[atom]:
        new_molecule = "".join(atoms[:i]) + replacement + "".join(atoms[i + 1 :])
        result.add(new_molecule)

print(len(result))
