
while True:
    answer = 'yes'
    stack = []
    string = input()
    if string == '.':
        break
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] == '[':
                answer = "no"
                break
            elif stack[-1] == '(':
                stack.pop()
        elif s == ']':
            if not stack or stack[-1] == '(':
                answer = "no"
                break
            elif stack[-1] == '[':
                stack.pop()

    if answer == 'yes' and not stack:
        print(answer)
    else:
        print('no')