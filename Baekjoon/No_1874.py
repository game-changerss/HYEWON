import sys

n = int(sys.stdin.readline())
#�Է°���

stack = [1] #�Է°��� ���� ����
num = 2 #���ÿ� ���� ����(1�� ����)
answer_bool = "True" #�Է°��� ������ Ȯ���ϴ� �οﺯ��
answer = ['+'] #1push

for i in range(n):
    #n����ŭ a �Է¹���
    a = int(sys.stdin.readline())

    while num<=a: #�Է°����� �۰ų� ���������� num����
        #if num > n:
        #    break
        #if a not in stack:
        stack.append(num)
        answer.append('+') #push
        num += 1
  
    if a == stack[-1]: #���ø����� ���ڰ� �Է°��� ������ pop
        stack.pop()
        answer.append('-')
    else: #�Է°��� ���ø������� �ٸ��� false����
        answer_bool = "False"

if answer_bool == "False": 
    print("NO")
else:
    for j in answer:
        print(j)