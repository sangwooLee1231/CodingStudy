import sys
input = sys.stdin.readline

n, k = map(int, input().split())     # 동전 종류 수 n, 목표 값 k
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

total_coins = 0
for coin in coins:
    if k == 0:
        break
    use = k // coin
    total_coins += use
    k %= coin

print(total_coins)
