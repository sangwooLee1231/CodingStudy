import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

start = 0
end = max(budgets)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(min(b, mid) for b in budgets)

    if total <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
