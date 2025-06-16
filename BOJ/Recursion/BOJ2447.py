import sys
input = sys.stdin.readline

def draw_star(x, y, n):
    if n == 1:
        board[x][y] = '*'
        return
    div = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw_star(x + i * div, y + j * div, div)

N = int(input())
board = [[' ' for _ in range(N)] for _ in range(N)]
draw_star(0, 0, N)

for row in board:
    print(''.join(row))
