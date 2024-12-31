import sys

garbage_mode = False

with open(sys.argv[1], "r") as file:
    for line in file:
        line_score = 0
        depth = 0
        garbage_removed = 0
        i = 0
        while i < len(line.strip()):
            try:
                if line[i] == "!":
                    i += 1
                elif garbage_mode:
                    if line[i] == ">":
                        garbage_mode = False
                    else:
                        garbage_removed += 1
                elif line[i] == "<":
                    garbage_mode = True
                elif line[i] == "{":
                    depth += 1
                elif line[i] == "}":
                    line_score += depth
                    depth -= 1
                elif line[i] not in ",":
                    print(f"Unexpected character at {i}: {line[i]}")
            finally:
                i += 1
        print(f"Part 1: Line score is {line_score}")
        print(f"Part 2: {garbage_removed} garbage removed")
