T = int(input())
for _ in range(T):
    line = input()
    stk = []
    isVPS = True

    for ch in line:
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                isVPS = False
                break

    if stk:
        isVPS = False

    print("YES" if isVPS else "NO")
