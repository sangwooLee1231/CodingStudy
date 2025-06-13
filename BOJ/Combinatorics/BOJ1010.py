import math
import sys

input = sys.stdin.readline

def bino_coef_factorial(n, k):
    if k > n:
        n, k = k, n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    print(bino_coef_factorial(n, k))
