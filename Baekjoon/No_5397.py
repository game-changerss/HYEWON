L = int(input())

for i in range(L):
  str = input()
  left, right = [],[]

  for s in str:
    if s == '<':
        if left:
            right.append(left.pop())
            #Ŀ���� �������� �̵��ϸ� left������ ���ڿ��� right�������� �ű��
            #���� �߰��� ���ڿ��� left���ø������� �߰��ϸ�
            # "a b < c"�� �Էµ� ��� a b -> a c | b -> a c b�� ��µǾ� ����
    elif s == '>':
        if right:
            left.append(right.pop())
    elif s == '-':
        if left:
            left.pop()
    else:
        left.append(s)
  
  left.extend(reversed(right))
  #ex)���÷� AB<<C���� �ԷµǾ����� reversed�� ������������
  #������ CAB�� �Ǿ�������� CBA�� ���� -> '>' �� ���ٶ����� 0�ε����� �Ű����°Ծƴ϶� �������׸����� �߰��� �Ǳ⶧��
  print(''.join(left))