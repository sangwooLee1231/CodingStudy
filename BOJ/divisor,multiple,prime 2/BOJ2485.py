import sys
import math
from functools import reduce
input = sys.stdin.readline

n = int(input())
trees = [int(input()) for _ in range(n)]
trees.sort()

diffs = []
for i in range(n - 1):
    diffs.append(trees[i+1] - trees[i])

g = reduce(math.gcd, diffs)

total_slots = (trees[-1] - trees[0]) // g
answer = total_slots - (n - 1)

print(answer)
