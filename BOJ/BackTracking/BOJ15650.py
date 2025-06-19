import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

def backtrack(start, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n + 1):
        result.append(i)
        backtrack(i + 1, depth + 1)
        result.pop()

backtrack(1, 0)
