import math
import sys

input = sys.stdin.readline

def bino_coef_factorial(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n,k = map(int, input().split())

print(bino_coef_factorial(n,k))