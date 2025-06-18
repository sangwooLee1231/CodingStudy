import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '.':
        break

    stack = []
    isVPS = True

    for ch in line:
        if ch == '(' or ch == '[':
            stack.append(ch)

        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                isVPS = False
                break

        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                isVPS = False
                break

    if stack:
        isVPS = False

    print("yes" if isVPS else "no")
