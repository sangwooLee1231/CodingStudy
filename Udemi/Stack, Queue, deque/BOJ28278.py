import sys
input = sys.stdin.readline

t = int(input().rstrip())
s = []

for _ in range(t):
    z = input().split()
    a = int(z[0])
    if a == 1:
            s.append(int(z[1]))
    elif a == 2:
        if s:
            print(s.pop())
        else:
            print(-1)
    elif a==3:
        print(len(s))
    elif a==4:
        if s:
            print(0)
        else:
            print(1)
    elif a==5:
        if s:
            print(s[-1])
        else:
            print(-1)
    else:
        print("잘못된 입력입니다.")