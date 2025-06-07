import sys
input = sys.stdin.readline

n = int(input())
present = set()

for _ in range(n):
    name, status = input().split()
    if status == "enter":
        present.add(name)
    else:
        present.discard(name)


for name in sorted(present, reverse=True):
    print(name)
