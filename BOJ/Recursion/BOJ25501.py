import sys
input = sys.stdin.readline

def recursion(s, l, r, cnt):
    cnt += 1
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 0)

n = int(input())
for _ in range(n):
    word = input().strip()
    result, count = isPalindrome(word)
    print(result, count)
