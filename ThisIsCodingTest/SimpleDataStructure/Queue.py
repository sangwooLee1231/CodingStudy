from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 파이썬으로 큐를 구현할 때에는 collections 모듈에서 제공하는 deque 사용
# 속도가 더 바르고, 코딩테스트 에서 앵간하면 허용하므로 사용하는거 추천