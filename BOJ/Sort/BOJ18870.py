import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sorted_unique = sorted(set(arr))

# enumerate -> 각각의 요소에 대해 (인덱스, 값) 쌍을 만들어줌
rank = {value: index for index, value in enumerate(sorted_unique)}

# 원래 입력받은 리스트 arr에 대해,
# 각 값 num을 rank[num]로 치환해서 새 리스트 result를 만든다
result = [rank[num] for num in arr]

# 리스트 result = [2, 3, 0, 3, 1]의 각 숫자를 문자열로 바꾸고
# ' '(공백)으로 이어붙여 출력함
print(' '.join(map(str, result)))
