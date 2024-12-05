from collections import defaultdict
import sys

requirements = defaultdict(set)
middle_numbers = 0

for line in sys.stdin:
    if "|" in line:
        required, requiring = line.split("|")
        requirements[int(requiring)].add(int(required))
    elif "," in line:
        pages = list(map(int, line.split(",")))
        printed = set()
        for p in pages:
            printable = True
            for required in requirements[p]:
                if required in pages and required not in printed:
                    # print(f"{line} is bogus!")
                    printable = False
                    break
            if not printable:
                break
            printed.add(p)
        if len(printed) == len(pages):
            print(f"We were able to print {line}")
            middle_numbers += pages[len(pages) // 2]

print(middle_numbers)
