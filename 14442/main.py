import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
a = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
dist = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def func():
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == N-1 and y == M-1:
            return dist[N-1][M-1][z]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if dist[nx][ny][z]:
                continue

            if a[nx][ny] == '0':
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            if a[nx][ny] == '1' and z < K:
                dist[nx][ny][z + 1] = dist[x][y][z] + 1
                q.append((nx, ny, z + 1))
    return -1

print(func())


