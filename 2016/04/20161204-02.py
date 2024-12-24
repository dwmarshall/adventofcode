from collections import Counter
import re
import sys


def valid_room(s: str) -> bool:
    m = re.match(r"(.*)-(\d+)\[([a-z]+)\]", s)
    room_name, _, checksum = m.groups()
    c = Counter(sorted(room_name))
    del c["-"]
    computed_checksum = "".join([x[0] for x in c.most_common(5)])
    return computed_checksum == checksum


def decrypt(s: str) -> str:
    m = re.match(r"(.*)-(\d+)", s)
    room_name, sector_id = m.groups()
    sector_id_val = int(sector_id)
    resultant = []
    for c in room_name:
        if c == "-":
            resultant.append(" ")
        else:
            offset = ord(c) - ord("a")
            offset += sector_id_val
            offset %= 26
            resultant.append(chr(offset + ord("a")))
    return "".join(resultant) + " " + sector_id


with open(sys.argv[1], "r") as file:
    for line in file:
        if not valid_room(line):
            continue
        print(decrypt(line))
