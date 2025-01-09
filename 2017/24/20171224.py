import sys

pieces = []
with open(sys.argv[1], "r") as file:
    for line in file:
        end1, end2 = map(int, line.strip().split("/"))
        pieces.append((end1, end2))

# A bridge is a tuple of pieces that have already been added, the current
# end port type, and a set of the available pieces

completed_bridges = set()
bridges = [(tuple(), 0, set(range(len(pieces))))]

while bridges:
    new_bridges = []
    for b in bridges:
        current_bridge, port, available_pieces = b
        if len(current_bridge) > 0:
            completed_bridges.add(current_bridge)
        matching_pieces = [x for x in available_pieces if port in pieces[x]]
        for m in matching_pieces:
            new_piece = pieces[m]
            new_bridge = list(current_bridge)
            new_bridge.append(new_piece)
            new_end1, new_end2 = new_piece
            new_port = new_end1 if port == new_end2 else new_end2
            new_available = available_pieces.copy()
            new_available.remove(m)
            new_bridges.append((tuple(new_bridge), new_port, new_available))

    bridges = new_bridges

best_bridge = max(sum(a + b for a, b in c) for c in completed_bridges)
print(f"Part 1: The strongest bridge is {best_bridge}.")

max_length = max(len(c) for c in completed_bridges)
best_bridge = max(
    sum(a + b for a, b in c) for c in completed_bridges if len(c) == max_length
)
print(f"Part 2: The strongest bridge of length {max_length} is {best_bridge}.")
