# import sys
# input = sys.stdin.readline
#
# m = int(input())  # 숫자 개수 입력
# num = []
# prime_number = dict()
#
# # 입력 받은 숫자들 저장
# for _ in range(m):
#     n = int(input())
#     num.append(n)
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# for nums in num:
#     if is_prime(nums):
#         prime_number[nums] = True
#
# print(prime_number)

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    while True:
        if is_prime(n):
            print(n)
            break
        n += 1
