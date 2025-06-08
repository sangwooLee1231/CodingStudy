# 반복으로 구현한 팩토리얼

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀로 구현한 팩토리얼

def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_reculsive(n-1)

print('반복으로 구현', factorial_iterative(5))
print('재귀로 구현', factorial_recursive(5))

# 반복보다 재귀로 했을 때, 속도가 더 빠름
# 재귀함수는 반복문을 이용하는 것과 비교했을 때 더욱 간결한 형태임