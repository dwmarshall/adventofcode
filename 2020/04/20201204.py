from collections.abc import Callable
import sys

REQUIRED_KEYS = set("byr,iyr,eyr,hcl,hgt,ecl,pid".split(","))


def passport_fields(s: str) -> dict[str, str]:
    return {k: v for f in s.split() for k, v in [f.split(":")]}


def date_validator(least: int, most: int) -> Callable:
    def validator(s: str) -> bool:
        return len(s) == 4 and least <= int(s) <= most

    return validator


def valid_hgt(s: str) -> bool:
    value = int(s[:-2])
    match s[-2:]:
        case "cm":
            return 150 <= value <= 193
        case "in":
            return 59 <= value <= 76
        case _:
            return False


def valid_hcl(s: str) -> bool:
    return s[0] == "#" and all(c in "0123456789abcdef" for c in s[1:])


def valid_ecl(s: str) -> bool:
    return s in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def valid_pid(s: str) -> bool:
    return len(s) == 9 and all(c in "0123456789" for c in s)


validators = {
    "byr": date_validator(1920, 2002),
    "iyr": date_validator(2010, 2020),
    "eyr": date_validator(2020, 2030),
    "hgt": valid_hgt,
    "hcl": valid_hcl,
    "ecl": valid_ecl,
    "pid": valid_pid,
}


def valid(p: dict[str, str]) -> bool:
    pf = passport_fields(p)
    if set(pf.keys()) - {"cid"} != REQUIRED_KEYS:
        return False
    return all(validators[f](pf[f]) for f in REQUIRED_KEYS)


with open(sys.argv[1], "r") as file:
    passports = file.read(None).split("\n\n")

p1_valid = 0
for p in passports:
    p_fields = set(passport_fields(p).keys())
    if p_fields - {"cid"} == REQUIRED_KEYS:
        p1_valid += 1

print(f"Part 1: There are {p1_valid} valid passports")

p2_valid = 0
for p in passports:
    if valid(p):
        p2_valid += 1

print(f"Part 2: There are {p2_valid} valid passports")
