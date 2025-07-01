import sys
input = sys.stdin.readline

str_word = input().strip()
n = int(input())

for _ in range(n):
    word, a, b = input().split()
    a = int(a)
    b = int(b)

    substring = str_word[a:b+1]
    cnt = substring.count(word)

    print(cnt)
