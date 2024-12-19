from functools import cache
import sys

available = []


@cache
def ways(s: str) -> bool:
    if s == "":
        return 1
    answer = 0
    for choice in available:
        if s == choice:
            answer += 1
        elif s.startswith(choice):
            answer += ways(s[len(choice) :])
    return answer


wanted = []

with open(sys.argv[1], "r") as file:
    line = file.readline()
    available = line.strip().split(", ")
    file.readline()
    for line in file:
        wanted.append(line.strip())

total_ways = 0

for w in wanted:
    this_answer = ways(w)
    print(f"We can make {w} in {this_answer} ways")
    total_ways += this_answer

print(total_ways)
