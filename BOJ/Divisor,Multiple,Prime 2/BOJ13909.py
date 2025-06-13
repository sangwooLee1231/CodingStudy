import sys
input = sys.stdin.readline

n = int(input())

window = [0] * n
i = 1
while True:
    if i == n:
        break
    for j in range (n):
