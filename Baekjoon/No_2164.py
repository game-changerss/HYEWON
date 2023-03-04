from collections import deque

N = int(input())
stack = deque([i+1 for i in range(N)])
#N이 4가 들어올경우 stack = [1,2,3,4]

if N > 2: 
    for i in range(N-2):
        stack.popleft()
        stack.append(stack.popleft())

if len(stack) == 2: #남은 카드가 두개면
    stack.popleft()

print(stack.pop()) #마지막남은 카드 숫자 출력