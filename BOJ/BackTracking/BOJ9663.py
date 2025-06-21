import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

col = [False] * n
diag1 = [False] * (2*n)
diag2 = [False] * (2*n)


def backtrack(row):
    global cnt
    if row== n:
        cnt+=1
    for c in range(n):
        if not col[c] and not diag1[row+c] and not diag2[row -c +n - 1]:
            col[c] = diag1[row + c] = diag2[row - c + n - 1] = True
            backtrack(row+1)
            col[c] = diag1[row + c] = diag2[row - c + n - 1] = False

# Queen은 행으로도 움직일 수 있지만, 백트래킹은 한 행에 하나의 queen만 들어간다는 것을
# 알기 때문에 굳이 행은 체크 안함

backtrack(0)
print(cnt)
