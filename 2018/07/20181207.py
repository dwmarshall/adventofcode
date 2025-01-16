from collections import defaultdict
import heapq
import re
import sys

AUTOMATIC_DELAY = 60
ELVES = 5


def time_required(s: str) -> int:
    assert len(s) == 1
    return AUTOMATIC_DELAY + 1 + ord(s) - ord("A")


graph = defaultdict(list)

with open(sys.argv[1], "r") as file:
    for line in file:
        if m := re.search(r"([A-Z]) must be finished before step ([A-Z])", line):
            graph[m.group(1)].append(m.group(2))

incoming = defaultdict(int, {x: 0 for x in graph})
for v in graph.values():
    for node in v:
        incoming[node] += 1

unvisited = set(incoming)
topological_sort = []

while unvisited:
    zero_incoming = {k for k, v in incoming.items() if incoming[k] == 0}
    curr = min(list(unvisited & zero_incoming))
    topological_sort.append(curr)
    unvisited.remove(curr)
    for node in graph[curr]:
        incoming[node] -= 1

print(f"Part 1: Correct order is {"".join(topological_sort)}")

# Part 2

elf_work = [None] * ELVES

incoming = defaultdict(int, {x: 0 for x in graph})
for v in graph.values():
    for node in v:
        incoming[node] += 1

unscheduled = set(incoming)

work_queue = []

available_jobs = [x for x in incoming if incoming[x] == 0]
for j in available_jobs:
    heapq.heappush(work_queue, (time_required(j), j))
    unscheduled.remove(j)

t = 0
while work_queue or any(w is not None for w in elf_work):
    # Clear out any completed jobs
    for i, task in enumerate(elf_work):
        if task is None:
            continue
        time_finished, job = task
        if time_finished == t:
            print(f"Job {job} was finished by elf {i} at time {t}")
            elf_work[i] = None
            # Delete the job's dependencies
            for node in graph[job]:
                incoming[node] -= 1
    # Identify jobs that can be queued
    zero_incoming = {k for k, v in incoming.items() if incoming[k] == 0}
    for j in zero_incoming & unscheduled:
        print(f"Time {t}: Job {j} is ready to be added to the queue")
        heapq.heappush(work_queue, (time_required(j), j))
        unscheduled.remove(j)
    # Assign any jobs that are available
    while work_queue and None in elf_work:
        elf = elf_work.index(None)
        time_needed, job = heapq.heappop(work_queue)
        elf_work[elf] = (t + time_needed, job)
        print(f"Assigned job {job} to elf {elf} at time {t}")
    t += 1

print(f"Part 2: It takes {t - 1} seconds to process the queue.")
