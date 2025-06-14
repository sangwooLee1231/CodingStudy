import sys

input = sys.stdin.readline

n = int(input())
dance_set = set()
dance_set.add("ChongChong")

for _ in range(n):
    a, b = input().strip().split()

    if a in dance_set or b in dance_set:
        dance_set.add(a)
        dance_set.add(b)

print(len(dance_set))
