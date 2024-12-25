import re
import sys

input = sys.stdin.readline().strip()

i = 0
uncompressed_length = 0

while i < len(input):
    if m := re.match(r"\((\d+)x(\d+)\)", input[i:]):
        i += m.span(0)[1]
        length, times = list(map(int, m.groups()))
        uncompressed_length += length * times
        i += length
    elif m := re.match(r"[^(]+", input[i:]):
        i += m.span(0)[1]
        uncompressed_length += m.span(0)[1]

print(uncompressed_length)
