from hashlib import md5
from itertools import count
import sys

INPUT = sys.argv[1]

password = [None] * 8

for i in count(1):
    key = f"{INPUT}{i}"
    digest = md5(key.encode()).hexdigest()
    if digest.startswith("00000"):
        pos = int(digest[5], 16)
        if pos < 8 and password[pos] is None:
            password[pos] = digest[6]
    if all(x is not None for x in password):
        break

print("".join(password))
