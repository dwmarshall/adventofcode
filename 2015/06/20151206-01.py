import re
import sys
from typing import Callable, Tuple

N = 1000

command = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")

lights = [[0] * N for _ in range(N)]


def turn_on(x: int, y: int) -> None:
    lights[x][y] = 1


def turn_off(x: int, y: int) -> None:
    lights[x][y] = 0


def toggle(x: int, y: int) -> None:
    lights[x][y] ^= 1


def apply(
    mutator: Callable, start_pos: Tuple[int, int], end_pos: Tuple[int, int]
) -> None:
    for x in range(start_pos[0], end_pos[0] + 1):
        for y in range(start_pos[1], end_pos[1] + 1):
            mutator(x, y)


for line in sys.stdin:
    this_command = command.match(line)
    start_pos = list(map(int, this_command.group(2, 3)))
    end_pos = list(map(int, this_command.group(4, 5)))
    match this_command.group(1):
        case "turn on":
            apply(turn_on, start_pos, end_pos)
        case "turn off":
            apply(turn_off, start_pos, end_pos)
        case "toggle":
            apply(toggle, start_pos, end_pos)

print(sum(sum(lights[i]) for i in range(N)))
