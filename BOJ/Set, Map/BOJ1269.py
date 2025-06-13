import sys
input = sys.stdin.readline

n,m = map(int,input().split())
set1 = set()
set2 = set()
list1 = input().split()
list2 = input().split()

for lists in list1:
    set1.add(lists)

for lists in list2:
    set2.add(lists)

count1 = len(set1-set2)
count2 = len(set2-set1)
result = count1 + count2
print(result)

# GPT가 달아준 더 나은 코드
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# set1 = set(map(int, input().split()))
# set2 = set(map(int, input().split()))
#
# # 방법 1: 대칭 차집합 연산
# result = len(set1 ^ set2)
#
# # 방법 2: 수작업으로
# # result = len(set1 - set2) + len(set2 - set1)
#
# print(result)
