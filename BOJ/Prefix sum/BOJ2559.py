import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

current_sum = sum(temps[:k])
max_sum = current_sum

for i in range(k, n):
    current_sum = current_sum - temps[i - k] + temps[i]
    max_sum = max(max_sum, current_sum)

print(max_sum)
