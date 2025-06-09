import sys
input = sys.stdin.readline

def get_divisors(n):
    return {i for i in range(1, n + 1) if n % i == 0}

m = int(input())
sets = []
nums = []

for _ in range(m):
    a, b = map(int, input().split())
    sets.append(get_divisors(a))
    sets.append(get_divisors(b))
    nums.append((a, b))

for i in range(0, len(sets), 2):
    gcd = max(sets[i] & sets[i+1])
    a, b = nums[i // 2]
    lcm = a * b // gcd
    print(lcm)


# GPT가 알려준 모범답안
# math 라이브러리에 이미 gcd()로 최대공약수를 구하는 함수가 있음
# import sys
# import math
# input = sys.stdin.readline
#
# T = int(input())  # 테스트 케이스 수
#
# for _ in range(T):
#     a, b = map(int, input().split())
#     lcm = a * b // math.gcd(a, b)
#     print(lcm)
