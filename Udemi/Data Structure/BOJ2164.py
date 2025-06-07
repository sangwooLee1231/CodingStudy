from collections import deque
t = deque()

a = int(input())

for i in range(a):
    t.append(i+1)

while len(t) > 1:
    t.popleft()
    t.append(t.popleft())

print(t[0])