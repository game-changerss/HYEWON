L,R = input().split()
strings = list(input())

quarter = [['q','w','e','r','t','y','u','i','o','p'],
           ['a','s','d','f','g','h','j','k','l'],
           ['z','x','c','v','b','n','m']]
size = 3 #자판 x좌표 크기
time = 0

for i in range(size):
    if L in quarter[i]: #왼손 위치
        Lx1 = i
        Ly1 = quarter[i].index(L)
    if R in quarter[i]: #오른손 위치
        Rx1 = i
        Ry1 = quarter[i].index(R)


for s in strings:
    if s in ['q','w','e','r','t','a','s','d','f','g','z','x','c','v']:
        for j in range(size):
            if s in quarter[j]:
                Lx2 = j
                Ly2 = quarter[j].index(s)

                time += abs(Lx1-Lx2) + abs(Ly1-Ly2)
                Lx1 = Lx2
                Ly1 = Ly2

    else:
        for z in range(size):
            if s in quarter[z]:
                Rx2 = z
                Ry2 = quarter[z].index(s)

                time += abs(Rx1-Rx2) + abs(Ry1-Ry2)
                Rx1 = Rx2
                Ry1 = Ry2

    time += 1 #각 키당 시간1 추가

print(time)