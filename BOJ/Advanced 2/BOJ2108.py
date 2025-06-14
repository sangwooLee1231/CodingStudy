import math
import sys

input = sys.stdin.readline

m = int(input())
stat = []

for _ in range (m):
    n = int(input())
    stat.append(n)

stat.sort()
avg = round(sum(stat) / len(stat))
middle = len(stat) // 2

freq = dict()
for num in stat:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_freq = max(freq.values())

modes = [k for k, v in freq.items() if v == max_freq]
modes.sort()

mode = modes[1] if len(modes) >= 2 else modes[0]

rng = stat[-1] - stat[0]

print(avg)
print(stat[middle])
print(mode)
print(rng)