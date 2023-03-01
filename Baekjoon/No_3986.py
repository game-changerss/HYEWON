N = int(input())
cnt = 0

for i in range(N):
    stack = []
    
    string = input()
    for s in string:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    
    if stack == []:
        cnt += 1

print(cnt)