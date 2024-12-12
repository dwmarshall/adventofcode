import json
import sys


def evaluate(e: object) -> None:
    global grand_total
    if type(e) is dict:
        parse_dict(e)
    elif type(e) is list:
        parse_list(e)
    elif type(e) is int:
        grand_total += int(e)


def parse_dict(d: dict) -> None:
    if "red" in d.values():
        return
    for v in d.values():
        evaluate(v)


def parse_list(L: list) -> None:
    for x in L:
        evaluate(x)


grand_total = 0

with open(sys.argv[1], "r") as file:
    doc = json.load(file)
    evaluate(doc)

print(grand_total)
