import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
moves = list(map(int, input().split()))

dq = deque((i+1, moves[i]) for i in range(n))
answer = []

while dq:
    idx, val = dq.popleft()
    answer.append(idx)

    if not dq:
        break

    if val > 0:
        dq.rotate(-(val-1))
    else:
        dq.rotate(-val)

print(' '.join(map(str, answer)))
