stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

# 파이썬에서 스택을 이용할 때 별도의 라이브러리가 필요 X
# 기본 리스트에서 append와 pop을 이용ㅇ하여 구현
# append는 리스트의 가장 뒤쪽에 데이터를 삽입하고
# pop은 리스트의 가장 뒤쪽에서 데이터를 꺼냄