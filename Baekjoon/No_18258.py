import sys

dic = {}
n, m = map(int,input().split())

for i in range(n):
  a = input()
  dic[a] = i+1
#print(dic)
reverse_dic = dict(map(reversed,dic.items()))
#reverse_dic = {v:k for k,v in dic.items()}
#print(reverse_dic)

for j in range(m):
  b = input()
  if b.isdigit():
    print(reverse_dic[int(b)])
    #print(reverse_dic.get(b))
  else:
    print(dic[b])

#a = sys.stdin.readline().split()#