import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
# 한 줄에 숫자들이 공백으로 구분되어 들어올 때
x = list(map(int, input().split()))

result = 0
x.sort()
first = x[n-1]
second = x[n-2]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m=m-1
    if m == 0:
        break
    result += second
    m = m-1


print(result)

