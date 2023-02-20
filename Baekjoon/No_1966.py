import sys
from collections import deque
#1966
n = int(input())
for i in range(n):
    c, idx = map(int,input().split())
    q = deque(list(map(int,sys.stdin.readline().split())))
    cnt = 0
    
    while q:
        m = max(q)
        front = q.popleft()
        idx -= 1

        if m == front:
            cnt += 1
            if idx < 0:
                print(cnt)
                break
        else:
            q.append(front)
            if idx<0:
                idx = len(q)-1