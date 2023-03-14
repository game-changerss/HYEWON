from collections import deque

N = int(input())
stack = deque([i+1 for i in range(N)])
#N�� 4�� ���ð�� stack = [1,2,3,4]

if N > 2: 
    for i in range(N-2):
        stack.popleft()
        stack.append(stack.popleft())

if len(stack) == 2: #���� ī�尡 �ΰ���
    stack.popleft()

print(stack.pop()) #���������� ī�� ���� ��