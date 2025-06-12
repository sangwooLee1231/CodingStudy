import sys
import math
input = sys.stdin.readline

def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n,m = map(int,input().split())

for num in range(n,m+1):
    if isPrime(num):
        print(num)
    num += 1
