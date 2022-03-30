import sys

N = int(sys.stdin.readline())

nMap = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
chkNo = [[False for _ in range(N)] for _ in range(N)]
chkYes = [[False for _ in range(N)] for _ in range(N)]


no = 0
yes = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for i in range(N):
    for j in range(N):
        if not chkNo[i][j]:
            c = nMap[i][j]

            que = [[i, j]]

            while que:
                x, y = que.pop(0)

                if chkNo[x][y]:
                    continue
                else:
                    chkNo[x][y] = True

                for t in range(4):
                    if 0 <= x + dx[t] < N and 0 <= y + dy[t] < N and nMap[x + dx[t]][y + dy[t]] == c and not chkNo[x + dx[t]][y + dy[t]]:
                        que.append([x + dx[t], y + dy[t]])

            no += 1

for i in range(N):
    for j in range(N):
        if nMap[i][j] == 'R':
            nMap[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if not chkYes[i][j]:
            c = nMap[i][j]

            que = [[i, j]]

            while que:
                x, y = que.pop(0)

                if chkYes[x][y]:
                    continue
                else:
                    chkYes[x][y] = True

                for t in range(4):
                    if 0 <= x + dx[t] < N and 0 <= y + dy[t] < N and nMap[x + dx[t]][y + dy[t]] == c and not chkYes[x + dx[t]][y + dy[t]]:
                        que.append([x + dx[t], y + dy[t]])

            yes += 1


print(no, yes)
