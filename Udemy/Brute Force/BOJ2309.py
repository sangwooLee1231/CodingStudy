
import sys
from itertools import combinations

input = sys.stdin.readline
v = []

for _ in range (9):
    x = int(input())
    v.append(x)

v1 = sorted(v)

for i in combinations(v1,7):
    if sum(i) == 100:
        for height in i:
            print(height)
        break;
