import sys
input = sys.stdin.readline

n = int(input())  # 숫자의 개수
numbers = list(map(int, input().split()))  # 수열
operators = list(map(int, input().split()))  # +, -, *, // 개수

max_result = -int(1e9)
min_result = int(1e9)

def backtrack(depth, total, plus, minus, mul, div):
    global max_result, min_result

    if depth == n:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return

    if plus:
        backtrack(depth + 1, total + numbers[depth], plus - 1, minus, mul, div)
    if minus:
        backtrack(depth + 1, total - numbers[depth], plus, minus - 1, mul, div)
    if mul:
        backtrack(depth + 1, total * numbers[depth], plus, minus, mul - 1, div)
    if div:
        if total < 0:
            backtrack(depth + 1, -(-total // numbers[depth]), plus, minus, mul, div - 1)
        else:
            backtrack(depth + 1, total // numbers[depth], plus, minus, mul, div - 1)

backtrack(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(max_result)
print(min_result)
