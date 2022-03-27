import sys


N, M = map(int, sys.stdin.readline().split())
nMap = [0] * N

for i in range(N):
    nMap[i] = list(sys.stdin.readline()[:-1])


print(nMap)


