from collections import deque
import sys

PLAYERS = int(sys.argv[1])
LAST_MARBLE = int(sys.argv[2])

scores = [0] * PLAYERS

# current marble is always next to last, so the new marble
# is always appendleft
circle = deque([0])

for i in range(1, LAST_MARBLE + 1):
    if i % 23 == 0:
        player = i % PLAYERS
        scores[player] += i + circle[-9]
        del circle[-9]
        circle.rotate(6)
    else:
        circle.appendleft(i)
        circle.rotate(-2)

print(
    f"Part 1: With {PLAYERS} players and marbles up to {LAST_MARBLE}, the winning score is {max(scores)}"
)
