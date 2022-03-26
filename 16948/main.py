import sys

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

que = []

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

nMap = [[1000000 for _ in range(N)] for _ in range(N)]

nMap[r1][c1] = 0
que.append([r1, c1])

while len(que):
    x, y = que.pop(0)

    for i in range(6):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and nMap[x + dx[i]][y + dy[i]] > nMap[x][y] + 1:
            nMap[x + dx[i]][y + dy[i]] = nMap[x][y] + 1
            que.append([x + dx[i], y + dy[i]])

if nMap[r2][c2] == 1000000:
    print(-1)
else:
    print(nMap[r2][c2])


