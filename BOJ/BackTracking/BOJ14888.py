import sys
input = sys.stdin.readline

n = int(input())

num = map(int,input().split())
oper = map(int,input().split())
nums = []

def backtrack(depth):
    if depth == m:
        print(max(nums))
        print(min(nums))
        return
    for i in range(1, len(num)+1):
# ing