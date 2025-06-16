import sys

input = sys.stdin.readline

def cantor_set(n):
    cantor = ['-'] * (3 ** n)

    def generate_set(start, end, level):
        if level == n:
            return
        mid_start = start + (end - start) // 3
        mid_end = end - (end - start) // 3
        for i in range(mid_start, mid_end):
            cantor[i] = ' '
        generate_set(start, mid_start, level + 1)
        generate_set(mid_end, end, level + 1)

    generate_set(0, len(cantor), 0)
    return ''.join(cantor)

while True:
    try:
        m = int(input())
        print(cantor_set(m))
    except EOFError:
        break
