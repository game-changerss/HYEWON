import sys
from collections import deque

n = int(input())
q= deque()
for i in range(n):
    a = sys.stdin.readline().strip().split(' ')
    if a[0] == 'push_front':
        q.appendleft(a[1])
    elif a[0] == 'push_back':
        q.append(a[1])
    elif a[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif a[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])###