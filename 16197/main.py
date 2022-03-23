import sys

def func():




N, M = map(int, sys.stdin.readline().split())

nMap = []

coin = []

for i in range(N):
    nMap.append(list(sys.stdin.readline().split()))
    for j in range(M):
        if nMap[i][j] == 'o':
            coin.append([i,j])






