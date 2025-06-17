n = int(input())
array = []

for _ in range(n):
    a = int(input())
    array.append(a)

array = sorted(array, reverse= True)

for i in array:
    print(i, end = ' ')