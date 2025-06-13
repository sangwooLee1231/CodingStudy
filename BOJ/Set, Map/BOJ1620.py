import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_to_name = dict()
name_to_num = dict()

for i in range(1, n+1):
    name = input().strip()
    num_to_name[i] = name
    name_to_num[name] = i

for _ in range(m):
    query = input().strip()
    if query.isdigit():
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])
