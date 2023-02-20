string = list(input())

stack = []
tmp = 1
answer = 0

for s in range(len(string)):
    if string[s] == '(':
        stack.append(string[s])
        tmp *= 2
    elif string[s] == '[':
        stack.append(string[s])
        tmp *= 3
    elif string[s] == ')':
        if string[s-1] == '(':            
            answer += tmp
        if not stack or stack[-1]=='[':
            answer =0
            break
        stack.pop()
        tmp //= 2
    else:
        if string[s-1] == '[':
            answer += tmp
        if not stack or stack[-1]=='(':
            answer =0
            break
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)