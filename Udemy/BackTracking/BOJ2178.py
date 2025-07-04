import sys
from collections import deque

input = sys.stdin.readline

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]  # 개행 제거


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs():
    chk = [[False] * m for _ in range(n)]
    chk[0][0] = True
    dq = deque()
    dq.append((0, 0, 1))

    while dq:
        y, x, d = dq.popleft()

        if y == n - 1 and x == m - 1:
            return d

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, d + 1))

    return -1


print(bfs())
