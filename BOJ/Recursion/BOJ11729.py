import sys
input = sys.stdin.readline

moves = []

def hanoi(n, start, end):
    if n == 1:
        moves.append((start, end))
        return
    mid = 6 - start - end
    hanoi(n - 1, start, mid)
    moves.append((start, end))
    hanoi(n - 1, mid, end)

n = int(input())
hanoi(n, 1, 3)

print(len(moves))
for a, b in moves:
    print(a, b)
