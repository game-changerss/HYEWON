from sys import stdin
from itertools import combinations
import sys
from collections import deque

n = int(input())
building = []
answer = 0

#Æ²¸²
for i in range(n):
    a, b = map(int, input().split(' '))
    if b == 0:
        answer += len(building)
        building.clear()
    elif b not in building:
        building.append(b)

answer += len(building)
print(answer)
