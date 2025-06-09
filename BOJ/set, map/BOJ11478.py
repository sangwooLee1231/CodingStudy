s = input().strip()
n = len(s)
substrings = set()

for i in range(n):
    for j in range(i+1, n+1):
        substrings.add(s[i:j])

print(len(substrings))


# # GPT가 알려준 모범답안
# def make_suffix_array(s):
#     return sorted([s[i:] for i in range(len(s))])


# def make_lcp_array(suffix_array):
#     lcp = [0]
#     for i in range(1, len(suffix_array)):
#         a, b = suffix_array[i-1], suffix_array[i]
#         cnt = 0
#         for x, y in zip(a, b):
#             if x == y:
#                 cnt += 1
#             else:
#                 break
#         lcp.append(cnt)
#     return lcp
#
# s = input().strip()
# n = len(s)
#
# suffix_array = make_suffix_array(s)
# lcp = make_lcp_array(suffix_array)
#
# # 전체 가능한 부분 문자열 개수: n(n+1)/2 또는 직접 계산
# total = sum(len(suffix) for suffix in suffix_array)
# redundant = sum(lcp)
# print(total - redundant)
