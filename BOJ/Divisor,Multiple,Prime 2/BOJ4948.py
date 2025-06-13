import math
import sys
input = sys.stdin.readline

def isPrime(n):
    if n<2:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

while True:
    n = int(input())
    total = []
    if n==0:
        break
    for num in range(n+1,2*n+1):
        if isPrime(num):
            total.append(num)
    print(len(total))
