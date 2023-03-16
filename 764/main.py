import sys
from itertools import combinations


#각 치킨집에서 모든 집까지의 거리의 합을 구한다. 거리의 합을 정렬한다. 0~ M-1 까지 더한다.

N, M = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
li1 = []
li2 = []
ansLi = []
len2 = 0

for i in range(N):
    for j in range(N):
        if li[i][j] == 1:
            li1.append([i, j])
        if li[i][j] == 2:
            li2.append([i, j])

combi = list(combinations(list(range(len(li2))), M))




