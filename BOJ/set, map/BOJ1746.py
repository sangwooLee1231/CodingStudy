import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict1 = dict()
dict2 = dict()

for i in range(n):
    a = input().strip()
    dict1[i] = a

for i in range(m):
    a = input().strip()
    dict2[i] = a

set1 = set(dict1.values())
set2 = set(dict2.values())

common = set1 & set2
count = len(common)
print(count)

for name in sorted(common):
    print(name)
