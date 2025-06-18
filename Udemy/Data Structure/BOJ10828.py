import heapq as hq
import sys
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    a = int(input())
    if a:
        hq.heappush(pq,(abs(a),a))
    else:
        print(hq.heappop(pq)[1] if pq else 0)

