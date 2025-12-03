import sys

first_password = 0
second_password = 0
curr = 50

with open(sys.argv[1], "r") as file:
    for line in file:
        steps = int(line[1:])
        second_password += steps // 100
        steps %= 100
        if line[0] == "L":
            if curr > 0 and steps > curr:
                second_password += 1
            curr -= steps
        else:
            if curr + steps > 100:
                second_password += 1
            curr += steps
        curr %= 100
        assert 0 <= curr < 100
        if curr == 0:
            first_password += 1
            second_password += 1

print(f"Part 1: The first password is {first_password}")
print(f"Part 2: The second password is {second_password}")
