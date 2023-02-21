from collections import deque

n, m = map(int, input().split())
cnt = 0
pop = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])

for p in pop:
    while True:
        if queue[0] == p:
            queue.popleft()
            break
        else:
            if queue.index(p) < len(queue)/2:
                while queue[0] != p:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != p:
                    queue.appendleft(queue.pop())
                    cnt += 1

print(cnt)