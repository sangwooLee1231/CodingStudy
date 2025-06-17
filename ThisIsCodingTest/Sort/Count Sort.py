array =  [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 계수정렬의 시간복잡도는 O(N+K)

# 파이썬의 기본 정렬 라이브러리인 sorted() 함수는 퀵 정렬과 동작 방식이 비슷한 병합 병렬 기반으로 만들어짐