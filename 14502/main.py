import sys


def func():
    que = list(v)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    chk = [[False for _ in range(M)] for _ in range(N)]

    while len(que):#2가 퍼져나가는 부분
        x, y = que.pop(0)

        if chk[x][y]:
            continue
        else:
            chk[x][y] = True

        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                if nMap[x + dx[i]][y + dy[i]] == 0:
                    que.append([x + dx[i], y + dy[i]])

    two = 0

    for i in range(N):
        for j in range(M):
            if chk[i][j]:
                two += 1

    return two


N, M = map(int, sys.stdin.readline().split())
ans = 0

nMap = [0] * N
r = []
v = []
l = 0
cnt = 0

for i in range(N):
    nMap[i] = list(map(int, sys.stdin.readline().split()))

    for j in range(M):
        if nMap[i][j] == 0:
            r.append([i, j])
        elif nMap[i][j] == 2:
            v.append([i, j])
        else:
            cnt += 1


l = len(r)

for a in range(l):#3개 고르기
    for b in range(a + 1, l):
        for c in range(b + 1, l):
            nMap[r[a][0]][r[a][1]] = 1
            nMap[r[b][0]][r[b][1]] = 1
            nMap[r[c][0]][r[c][1]] = 1

            ans = max(ans, N * M - cnt - 3 - func())

            nMap[r[a][0]][r[a][1]] = 0
            nMap[r[b][0]][r[b][1]] = 0
            nMap[r[c][0]][r[c][1]] = 0

print(ans)
