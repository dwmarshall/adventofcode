import sys

nums = []

with open(sys.argv[1], "r") as file:
    for line in file:
        binary_length = len(line.strip())
        nums.append(int(line.strip(), 2))


gamma, epsilon = 0, 0

for i in range(binary_length):
    mask = 1 << i
    hits = [x for x in nums if x & mask != 0]
    if len(hits) >= len(nums) // 2:
        gamma |= mask
    else:
        epsilon |= mask
    i += 1

print(f"Part 1: The power consumption is {gamma * epsilon}")

# Part 2

o2_nums = nums.copy()
co2_nums = nums.copy()

for i in range(binary_length):
    mask = 1 << (binary_length - i - 1)
    if len(o2_nums) > 1:
        o2_ones = [x for x in o2_nums if x & mask != 0]
        o2_zeroes = [x for x in o2_nums if x & mask == 0]
        o2_nums = o2_ones if len(o2_ones) >= len(o2_zeroes) else o2_zeroes
    if len(co2_nums) > 1:
        co2_ones = [x for x in co2_nums if x & mask != 0]
        co2_zeroes = [x for x in co2_nums if x & mask == 0]
        co2_nums = co2_zeroes if len(co2_zeroes) <= len(co2_ones) else co2_ones


print(f"Part 2: The life support rating is {o2_nums[0] * co2_nums[0]}")
