import sys
input = sys.stdin.readline

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

m = int(input())

print(fac(m))