import sys
input = sys.stdin.readline


n,m = map(int,input().split())
result = []

def backtrack(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    start = result[-1] if result else 1
    for i in range(start, n+1):
            result.append(i)
            backtrack(depth + 1)
            result.pop()





backtrack(0)