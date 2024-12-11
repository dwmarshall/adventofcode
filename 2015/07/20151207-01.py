from collections import defaultdict
import operator
import re
import sys
from typing import Callable


values = dict()
symbol_map = dict()
symbols = []
graph = defaultdict(set)


def symbol_id(s: str) -> int:
    if s not in symbol_map:
        symbol_map[s] = len(symbol_map)
        symbols.append(s)
    return symbol_map[s]


def binary_closure(sym1: str, sym2: str, op: Callable) -> Callable:
    return lambda: op(values[sym1], values[sym2])


def shift_closure(sym1: str, num: int, op: Callable) -> Callable:
    return lambda: op(values[sym1], num)


def unary_closure(sym1: str, op: Callable) -> Callable:
    return lambda: op(values[sym1])


def identity_closure(sym1: str) -> Callable:
    return lambda: values[sym1]


ops = {
    "AND": operator.__and__,
    "LSHIFT": operator.__lshift__,
    "OR": operator.__or__,
    "NOT": operator.__invert__,
    "RSHIFT": operator.__rshift__,
}

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.match(r"(\d+) -> (\S+)", line):
            value, symbol = m.groups()
            id = symbol_id(symbol)
            values[symbol] = int(value)
            graph[id]
        elif m := re.match(r"(\S+) -> (\S+)", line):
            # print(line)
            sym1, sym2 = m.groups()
            id1 = symbol_id(sym1)
            id2 = symbol_id(sym2)
            values[sym2] = identity_closure(sym1)
            graph[id1].add(id2)
        elif m := re.match(r"(\d+) (AND|OR) (\S+) -> (\S+)", line):
            arg, op, sym1, sym2 = m.groups()
            id1 = symbol_id(sym1)
            id2 = symbol_id(sym2)
            values[sym2] = shift_closure(sym1, int(arg), ops[op])
            graph[id1].add(id2)
        elif m := re.match(r"(\S+) (AND|OR) (\S+) -> (\S+)", line):
            sym1, op, sym2, sym3 = m.groups()
            id1 = symbol_id(sym1)
            id2 = symbol_id(sym2)
            id3 = symbol_id(sym3)
            values[sym3] = binary_closure(sym1, sym2, ops[op])
            graph[id1].add(id3)
            graph[id2].add(id3)
        elif m := re.match(r"(\S+) (LSHIFT|RSHIFT) (\d+) -> (\S+)", line):
            sym1, op, arg, sym2 = m.groups()
            id1 = symbol_id(sym1)
            id2 = symbol_id(sym2)
            values[sym2] = shift_closure(sym1, int(arg), ops[op])
            graph[id1].add(id2)
        elif m := re.match(r"NOT (\S+) -> (\S+)", line):
            sym1, sym2 = m.groups()
            id1 = symbol_id(sym1)
            id2 = symbol_id(sym2)
            values[sym2] = unary_closure(sym1, ops["NOT"])
            graph[id1].add(id2)
        else:
            print("no match for:", line.strip())

unvisited = set(range(len(symbol_map)))
incoming = [0] * len(symbol_map)

for edges in graph.values():
    for e in edges:
        incoming[e] += 1

while unvisited:
    choices = set([x for x in range(len(incoming)) if incoming[x] == 0])
    choice = (unvisited & choices).pop()
    symbol = symbols[choice]
    if symbol in values and callable(values[symbol]):
        values[symbol] = values[symbol]()
    unvisited.discard(choice)
    for d in graph[choice]:
        incoming[d] -= 1

if "a" in values:
    print(values["a"])
else:
    print(values)
