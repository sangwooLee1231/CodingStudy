from collections import deque
import sys
input = sys.stdin.readline

q = deque()

def push(x):
    q.append(x)

def pop():
    if q:
        print(q.popleft())
    else:
        print(-1)

def size():
    print(len(q))

def empty():
    print(0 if q else 1)

def front():
    if q:
        print(q[0])
    else:
        print(-1)

def back():
    if q:
        print(q[-1])
    else:
        print(-1)

n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        push(int(cmd[1]))
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()
