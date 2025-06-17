array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 파이썬에서의 스왑(swap)

# array = [3,5]
# array[0], array[1] = array[1], array[0]
# 이런식으로 굳이 temp없이 스왑 가능
# 선택정렬의 시간복잡도 -> O(N^2)