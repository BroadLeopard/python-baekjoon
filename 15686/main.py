import sys
from itertools import combinations

ans = 1000000000
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if li[i][j] == 1:
            home.append([i, j])
        elif li[i][j] == 2:
            chicken.append([i, j])

combis = list(combinations(chicken, len(chicken) - M))# 부분은 지웠다가 다시 1로 되돌릴 예정

for combi in combis:
    tmp = 0

    for x, y in combi:
        li[x][y] = 0

    #이제 여기서 각 집에서 치킨까지 최소 거리를 구한다.
    for hx, hy in home:
        que = [[hx, hy]]

        while True:
            tx, ty = que.pop(0)

            if li[tx][ty] == 2:
                tmp += abs(tx - hx) + abs(ty - hy)
                break

            for i in range(4):
                if 0 <= tx + dx[i] < N and 0 <= ty + dy[i] < N:
                    que.append([tx + dx[i], ty + dy[i]])

    for x, y in combi:  # 2로 복구
        li[x][y] = 2

    ans = min(tmp, ans)


print(ans)