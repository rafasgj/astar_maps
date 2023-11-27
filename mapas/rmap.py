"""Generate a random map."""

import sys
from random import random


w = int(sys.argv[1] if len(sys.argv) > 1 else 30)
h = int(sys.argv[2] if len(sys.argv) > 2 else 30)

print(f"{w} {h}")
print(f"0 0")
for l in range(w):
    for c in range(h):
        print("{0: >3s}".format("0" if random() < 0.8 else "-1"), end="")
    print()

