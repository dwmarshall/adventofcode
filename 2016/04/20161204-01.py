from collections import Counter
import re
import sys


def room_value(s: str) -> int:
    m = re.match(r"(.*)-(\d+)\[([a-z]+)\]", s)
    room_name, value, checksum = m.groups()
    c = Counter(sorted(room_name))
    del c["-"]
    computed_checksum = "".join([x[0] for x in c.most_common(5)])
    return int(value) if computed_checksum == checksum else 0


total_sector_ids = 0
with open(sys.argv[1], "r") as file:
    for line in file:
        total_sector_ids += room_value(line.strip())

print(total_sector_ids)
