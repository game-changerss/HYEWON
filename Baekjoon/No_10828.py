import sys
def push(x):
  stack.append(x)

def pop():
  if len(stack) == 0:
    print(-1)
  else:
    print(stack.pop())

def size():
  print(len(stack))

def empty():
  if len(stack) == 0:
    print(1)
  else:
    print(0)

def top():
  if len(stack) == 0:
    print(-1)
  else:
    print(stack[-1])

stack = []
n = int(input())

for i in range(n):
  a = sys.stdin.readline().split()
  if a[0] == 'push':
    push(int(a[1]))
  elif a[0] == 'pop':
    pop()
  elif a[0] == 'size':
    size()
  elif a[0] == 'empty':
    empty()
  else:
    top()
