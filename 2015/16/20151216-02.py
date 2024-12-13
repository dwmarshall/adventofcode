import re


def matching(truth: dict, candidate: dict) -> bool:
    for k, v in candidate.items():
        if k in {"cats", "trees"}:
            if v <= truth[k]:
                return False
        elif k in {"pomeranians", "goldfish"}:
            if v >= truth[k]:
                return False
        elif truth[k] != v:
            return False
    return True


ticker = {}

with open("ticker.txt", "r") as file:
    for line in file:
        if m := re.match(r"(\S+): (\d+)", line):
            ticker[m.group(1)] = int(m.group(2))

with open("input.txt", "r") as file:
    for line in file:
        m = re.match(r"Sue (\d+)", line)
        sue = int(m.group(1))
        object = {}
        for k, v in re.findall(r"(\S+): (\d+)", line):
            object[k] = int(v)
        if matching(ticker, object):
            print(sue)
            break
