import sys

n = int(sys.stdin.readline())
#입력갯수

stack = [1] #입력값과 비교할 스택
num = 2 #스택에 넣을 숫자(1씩 증가)
answer_bool = "True" #입력값과 같은지 확인하는 부울변수
answer = ['+'] #1push

for i in range(n):
    #n개만큼 a 입력받음
    a = int(sys.stdin.readline())

    while num<=a: #입력값보다 작거나 같을때까지 num증가
        #if num > n:
        #    break
        #if a not in stack:
        stack.append(num)
        answer.append('+') #push
        num += 1
  
    if a == stack[-1]: #스택마지막 숫자가 입력값과 같으면 pop
        stack.pop()
        answer.append('-')
    else: #입력값과 스택마지막값 다르면 false저장
        answer_bool = "False"

if answer_bool == "False": 
    print("NO")
else:
    for j in answer:
        print(j)