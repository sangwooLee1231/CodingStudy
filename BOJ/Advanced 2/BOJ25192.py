import sys

input = sys.stdin.readline

m = int(input())
set1 = set()
count = 0

for _ in range(m):
    n = input().strip()

    if n == "ENTER":
        set1.clear()
    else:
        if n not in set1:
            count += 1
            set1.add(n)

print(count)
