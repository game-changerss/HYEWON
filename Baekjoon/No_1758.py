N = int(input())
tip = [0]*N
result = 0

for i in range(N):
    tip[i] = int(input())

tip.sort(reverse=True)

for j in range(N):
    check = tip[j]-j
    if check > 0:
        result += check

print(result)