import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
d = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
nMap = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d[0][0][0] = 1

for _ in range(N):
    nMap.append(list(sys.stdin.readline()[:-1]))


def func():
    deq = deque([[0, 0, 0]])

    while deq:
        x, y, z = deq.popleft()

        if x == N - 1 and y == M - 1:
            return d[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if nMap[nx][ny] == "0" and not d[nx][ny][z]:#벽이 아닐때
                d[nx][ny][z] = d[x][y][z] + 1
                deq.append([nx, ny, z])
            elif z == 0 and nMap[nx][ny] == "1":#벽이 맞고 벽을 부순 적이 없을때
                d[nx][ny][1] = d[x][y][0] + 1
                deq.append([nx, ny, 1])


    return -1

print(func())

