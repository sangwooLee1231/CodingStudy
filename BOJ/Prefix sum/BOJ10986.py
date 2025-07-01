# import sys
# input = sys.stdin.readline
#
# n,m = map(int,input().split())
# num_list = list(map(int,input().split()))
# cnt = 0
# j = 0
# while j < n:
#     num_sum = 0
#     for i in range(j, n):
#         num_sum += num_list[i]
#         if num_sum % m == 0:
#             cnt += 1
#     j += 1
#
# print(cnt)
# 시간 초과

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

prefix_mod = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_mod[i] = (prefix_mod[i-1] + num_list[i-1]) % m

count = 0
freq = [0] * m
for val in prefix_mod:
    count += freq[val]
    freq[val] += 1

print(count)
