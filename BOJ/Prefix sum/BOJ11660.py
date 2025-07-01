import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range (m):
    sum_sum = 0
    x1,y1,x2,y2 = map(int,input().split())
