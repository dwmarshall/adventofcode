import sys

eggnog = int(sys.argv[1])

containers = []

with open(sys.argv[2], "r") as file:
    for line in file:
        containers.append(int(line))

all_containers = set(range(len(containers)))

dp = [[] for _ in range(eggnog + 1)]
dp[0].append(set())

for i in range(eggnog):
    for s in dp[i]:
        for c in all_containers - s:
            new_index = i + containers[c]
            new_set = s | {c}
            if new_index <= eggnog and new_set not in dp[new_index]:
                dp[new_index].append(s | {c})

least = min([len(x) for x in dp[eggnog]])
print(len([x for x in dp[eggnog] if len(x) == least]))
