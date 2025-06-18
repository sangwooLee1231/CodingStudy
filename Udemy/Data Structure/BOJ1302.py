import sys
input = sys.stdin.readline

t = dict()
a = int(input())

for _ in range(a):
    book = input().rstrip()
    if book in t:
        t[book] = t[book] + 1
    else:
        t[book] = 1

m = max(t.values())
candi = []
for k,v in t.items():
    if v ==m:
        candi.append(k)
candi.sort()
print(candi[0])