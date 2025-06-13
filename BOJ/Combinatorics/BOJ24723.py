import sys

input = sys.stdin.readline

n = int(input())
result = 1

for _ in range(n):
    result = result * 2


print(result)