t = int(input())
stack = []

for i in range (t) :
  stack.clear()
  ps = input()
  for p in ps:
    if p == '(':
      stack.append('(')
    else:
      size = len(stack)
      if size <= 0:
        stack.append(')')
        break
      else:
        stack.pop()
        
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")
