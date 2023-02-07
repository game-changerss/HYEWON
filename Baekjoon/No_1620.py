import sys

dic = {}
n, m = map(int,input().split())

for i in range(n): #n길이만큼 사전에 값 저장
  a = input()
  dic[a] = i+1

reverse_dic = dict(map(reversed,dic.items()))
#키:값을 값:키로 뒤집기

#reverse_dic = {v:k for k,v in dic.items()}
#print(reverse_dic)

for j in range(m):
  b = input()
  if b.isdigit(): #숫자인경우 값:키로 뒤집은 사전으로 탐색
    print(reverse_dic[int(b)])
    #print(reverse_dic.get(b))
  else:
    print(dic[b])
