# import math
# import sys
# input = sys.stdin.readline
#
# def isPrime(n):
#     if n<2:
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
# while True:
#     n = int(input())
#     middle = n//2
#     j = n
#     count = 0
#     for i in range (n):
#         if isPrime(i) & isPrime(j):
#             count +=1
#         i +=1
#         j -=1
#         if i>middle:
#             break
#     print(count)

import sys
input = sys.stdin.readline

# 최대 n 값 (문제 제한: n ≤ 1,000,000)
MAX = 1_000_000

# 1) 에라토스테네스의 체로 소수 판별 배열 만들기
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

# 2) 입력받아서 각 n에 대해 파티션 개수 세기
T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    # p ≤ n-p 인 경우만 세면 중복 없이 셈
    for p in range(2, n//2 + 1):
        if is_prime[p] and is_prime[n - p]:
            cnt += 1
    print(cnt)
