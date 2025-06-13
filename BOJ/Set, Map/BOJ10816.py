import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

dic = dict()

for num in cards:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

result = []
for t in targets:
    result.append(str(dic.get(t, 0)))

print(' '.join(result))
