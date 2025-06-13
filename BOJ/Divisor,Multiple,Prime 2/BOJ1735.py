import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a * d + c * b
denominator = b * d

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

common_divisor = gcd(numerator, denominator)
numerator //= common_divisor
denominator //= common_divisor

print(numerator, denominator)
