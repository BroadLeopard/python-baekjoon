import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

shark = 2
cnt = 0
ans = 0



def func():
    global shark, cnt, x, y
    que2 = [[x, y]]
    li = []

    chk = [[False for _ in range(N)] for _ in range(N)]
    dis = [[0 for _ in range(N)] for _ in range(N)]

    while que2:
        tx, ty = que2.pop(0)

        if chk[tx][ty]:
            continue
        else:
            chk[tx][ty] = True

        for i in range(4):
            if 0 <= tx + dx[i] < N and 0 <= ty + dy[i] < N and not chk[tx + dx[i]][ty + dy[i]] and nMap[tx + dx[i]][ty + dy[i]] <= shark:

                if nMap[tx + dx[i]][ty + dy[i]] != 0 and nMap[tx + dx[i]][ty + dy[i]] < shark:
                    li.append([dis[tx][ty] + 1, tx + dx[i], ty + dy[i]])
                    chk[tx + dx[i]][ty + dy[i]] = True

                dis[tx + dx[i]][ty + dy[i]] = dis[tx][ty] + 1
                que2.append([tx + dx[i], ty + dy[i]])

    if li:
        li.sort()
        nMap[li[0][1]][li[0][2]] = 0
        x, y = li[0][1], li[0][2]
        cnt += 1

        if cnt == shark:
            shark += 1
            cnt = 0

        return li[0][0]
    else:
        return 0


x, y = 0, 0


N = int(sys.stdin.readline())

que = []
nMap = []


for i in range(N):
    nMap.append(list(map(int, sys.stdin.readline().split())))

    for j in range(N):
        if nMap[i][j] == 9:  # 상어 위치
            nMap[i][j] = 0
            x, y = i, j



while True:
    dis2 = func()

    if dis2 == 0:
        break
    else:
        ans += dis2





print(ans)


