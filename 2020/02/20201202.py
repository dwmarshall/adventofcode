from collections import Counter
import re
import sys

p1_valid = 0
p2_valid = 0

with open(sys.argv[1], "r") as file:
    for line in file:
        m = re.match(r"(\d+)-(\d+) ([a-z]): (.*)", line)
        minimum = int(m.group(1))
        maximum = int(m.group(2))
        letter = m.group(3)
        word = m.group(4)
        c = Counter(word)
        if minimum <= c[letter] <= maximum:
            p1_valid += 1
        if (word[minimum - 1] == letter) ^ (word[maximum - 1] == letter):
            p2_valid += 1

print(f"Part 1: There are {p1_valid} valid passwords.")
print(f"Part 2: There are {p2_valid} valid passwords")
