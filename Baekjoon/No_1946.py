from sys import stdin


for i in range(int(stdin.readline())):
    
    employee = []
    for j in range(int(stdin.readline())):
        a, b = list(map(int, stdin.readline().split(' ')))
        employee.append([a, b])

    employee.sort()
    f = 0
    result = 1

    for z in range(1, len(employee)):
        if employee[z][1] < employee[f][1]:
            f = z
            result +=1

    print(result)
