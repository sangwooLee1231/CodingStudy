import sys
input = sys.stdin.readline

q = []
n = int(input().rstrip())

for _ in range(n):
    a = int(input().rstrip())
    if a:
        q.append(a)
    else:
        q.pop()

count = 0
for i in range(len(q)):
    count = count + q[i]
print(count)