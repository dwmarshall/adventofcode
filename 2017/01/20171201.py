import sys


def captcha1(s: str) -> int:
    result = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            result += int(s[i])
    if s[0] == s[-1]:
        result += int(s[0])

    return result


def captcha2(s: str) -> int:
    result = 0
    for i in range(len(s)):
        j = (i + len(s) // 2) % len(s)
        if s[i] == s[j]:
            result += int(s[i])
    return result


with open(sys.argv[1], "r") as file:
    digits = file.readline()

print(f"Part 1: {captcha1(digits)}")
print(f"Part 2: {captcha2(digits)}")
