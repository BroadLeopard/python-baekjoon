import sys


ans = 0
N, M = map(int, sys.stdin.readline().split())


nMap = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
nMap2 = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
nMap3 = [[False for _ in range (M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if nMap[i][j] != nMap2[i][j]:
            nMap3[i][j] = True



for i in range(N - 2):
    for j in range(M - 2):
        if nMap3[i][j]:
            for k in range(3):
                for l in range(3):
                    nMap3[i + k][j + l] = not nMap3[i + k][j + l]
            ans += 1

for i in range(N):
    for j in range(M):
        if nMap3[i][j]:
            print(-1)
            exit(0)

print(ans)




