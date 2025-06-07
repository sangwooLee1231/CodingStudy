import sys
input = sys.stdin.readline

n = int(input())
ways = list(input().split())
x = 1
y = 1

for way in ways:
    if way == 'L' and x > 1:
        x = x-1
    elif way == 'R':
        x = x+1
    elif way == 'U' and y>1:
        y = y-1
    elif way == 'D':
        y = y+1
print(y,x)