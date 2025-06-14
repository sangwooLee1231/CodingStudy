import sys
input = sys.stdin.readline

n, m = map(int, input().split())
english_dict = dict()

# 단어 빈도 수 세기
for _ in range(n):
    en = input().strip()
    if len(en) >= m:
        if en in english_dict:
            english_dict[en] += 1
        else:
            english_dict[en] = 1

sorted_words = sorted(
    english_dict.items(),
    key=lambda x: (-x[1], -len(x[0]), x[0])
)

for word, _ in sorted_words:
    print(word)
