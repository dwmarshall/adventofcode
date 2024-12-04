import re
import sys

total_nice = 0

triple_vowel = re.compile(r"[aeiou].*[aeiou].*[aeiou]")
double_letter = re.compile(r"([a-z])\1")
bad_pairs = re.compile(r"ab|cd|pq|xy")

with open(sys.argv[1], "r") as file:
    for line in file:
        if triple_vowel.search(line) is None:
            continue
        if double_letter.search(line) is None:
            continue
        if bad_pairs.search(line) is not None:
            continue
        total_nice += 1

print(total_nice)
