from collections import deque

# 인접행렬
adj = [[0]*13 for _ in range (13)]
adj[0][1] = adj[0][7] =1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[3][4] = 1
adj[5][6] = 1


def bfs():
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)


bfs(0)