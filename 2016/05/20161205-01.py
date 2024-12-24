from hashlib import md5
from itertools import count
import sys

INPUT = sys.argv[1]

password = []

for i in count(1):
    key = f"{INPUT}{i}"
    digest = md5(key.encode()).hexdigest()
    if digest.startswith("00000"):
        password.append(digest[5])
    if len(password) == 8:
        break

print("".join(password))
