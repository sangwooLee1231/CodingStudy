import sys
import math
from functools import reduce

input = sys.stdin.readline

n = int(input())
measure = list(map(int, input().split()))

lcm = reduce(math.lcm, measure)
gcd = reduce(math.gcd, measure)

if lcm in measure:
    lcm = lcm * gcd

print(lcm)