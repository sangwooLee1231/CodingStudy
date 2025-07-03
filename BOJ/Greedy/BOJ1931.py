import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
current_end_time = 0

for start, end in meetings:
    if start >= current_end_time:
        count += 1
        current_end_time = end

print(count)
