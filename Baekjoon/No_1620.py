import sys

dic = {}
n, m = map(int,input().split())

for i in range(n): #n���̸�ŭ ������ �� ����
  a = input()
  dic[a] = i+1

reverse_dic = dict(map(reversed,dic.items()))
#Ű:���� ��:Ű�� ������

#reverse_dic = {v:k for k,v in dic.items()}
#print(reverse_dic)

for j in range(m):
  b = input()
  if b.isdigit(): #�����ΰ�� ��:Ű�� ������ �������� Ž��
    print(reverse_dic[int(b)])
    #print(reverse_dic.get(b))
  else:
    print(dic[b])
