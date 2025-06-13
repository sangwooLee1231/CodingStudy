import sys
input = sys.stdin.readline

x = int(input())
list1 = input().split()
a = int(input())
list2 = input().split()

for idx, item in enumerate(list2):
    if item in list1:
        list2[idx] = '1'
    else:
        list2[idx] = '0'

print(' '.join(list2))
