n, m = map(int, input().split())
x = set()
count = 0
for _ in range(n):
    s = input().strip()
    x.add(s)
for _ in range(m):
    y = input().strip()
    if y in x:
        count = count + 1

print(count)