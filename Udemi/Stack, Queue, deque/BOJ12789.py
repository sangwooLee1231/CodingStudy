import sys
input = sys.stdin.readline

n = []
x = int(input().rstrip())

for i in range(x):
    a = int(input().rstrip())
    if a == i+1:
        i = i+1
    else
        n.append