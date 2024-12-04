from hashlib import md5
from itertools import count

INPUT = "iwrupvqb"

for i in count(1):
    key = f"{INPUT}{i}"
    digest = md5(key.encode()).hexdigest()
    if digest.startswith("000000"):
        print(i)
        break
