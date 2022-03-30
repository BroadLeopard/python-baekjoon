import sys

W, H = map(int, sys.stdin.readline().split())
cnt = [[0 for _ in range(W)] for _ in range(H)]

C = []
whMap = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(H):
    whMap.append(list(sys.stdin.readline()[:-1]))
    for j in range(W):
        if whMap[i][j] == 'C':
            C.append([i, j])

cnt[C[0][0]][C[0][1]] = 0
que = [C[0]]

while que:
    x, y = que.pop(0)

    for i in range(4):
        k = 1

        while True:
            if 0 <= x + k*dx[i] < H and 0 <= y + k*dy[i] < W:
                if whMap[x + k*dx[i]][y + k*dy[i]] == '*':
                    break
                if cnt[x + k * dx[i]][y + k * dy[i]] == 0:
                    cnt[x + k * dx[i]][y + k * dy[i]] = cnt[x][y] + 1
                    que.append([x + k*dx[i], y + k*dy[i]])

                k += 1
            else:
                break


print(cnt[C[1][0]][C[1][1]] - 1)

