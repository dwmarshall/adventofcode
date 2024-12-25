import re
import sys

input = sys.stdin.readline().strip()

i = 0
uncompressed_length = 0


def decompressed_length(s: str) -> int:
    i = 0
    total_length = 0
    while i < len(s):
        if m := re.match(r"\((\d+)x(\d+)\)", s[i:]):
            marker_length = m.span(0)[1]
            length, times = list(map(int, m.groups()))
            total_length += times * decompressed_length(
                s[i + marker_length : i + marker_length + length]
            )
            i += marker_length + length
        elif m := re.match(r"[^(]+", s[i:]):
            i += m.span(0)[1]
            total_length += m.span(0)[1]
    return total_length


print(decompressed_length(input))
