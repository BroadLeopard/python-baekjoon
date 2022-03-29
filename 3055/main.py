import sys

R, C = map(int, sys.stdin.readline().split())
rcMap = []

dis = [[0 for _ in range(C)] for _ in range(R)]
chk = [[False for _ in range(C)] for _ in range(R)]
wChk = [[False for _ in range(C)] for _ in range(R)]


D = []
S = []
w = []

for i in range(R):
    rcMap.append(list(sys.stdin.readline()[:-1]))

    for j in range(C):
        if rcMap[i][j] == 'D':
            D = [i, j]
        elif rcMap[i][j] == 'S':
            S = [i, j]
        elif rcMap[i][j] == '*':
            w = [i, j]

que = [[S[0], S[1], 0]]
wque = [[w[0], w[1], 0]]
cur = 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cur = 0


while len(que):
    while len(que):
        if que[0][2] == cur:
            x, y, t = que.pop(0)

            if chk[x][y]:
                continue
            else:
                chk[x][y] = True


            for i in range(4):
                if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C and rcMap[x + dx[i]][y + dy[i]] != '*' and rcMap[x + dx[i]][y + dy[i]] != 'X' and not chk[x + dx[i]][y + dy[i]]:
                    #가려는 곳이 돌, 물 아니고 가본적이 없을때

                    if rcMap[x + dx[i]][y + dy[i]] == 'D':
                        dis[x + dx[i]][y + dy[i]] = dis[x][y] + 1
                        break


                    flag = True

                    for j in range(4):
                        if 0 <= x + dx[i] + dx[j] < R and 0 <= y + dy[i] + dy[j] < C and rcMap[x + dx[i] + dx[j]][y + dy[i] + dy[j]] == '*':#가려는 곳 주변에 물 있으면
                            flag = False
                            break

                    if flag:
                        dis[x + dx[i]][y + dy[i]] = dis[x][y] + 1
                        que.append([x + dx[i], y + dy[i], t + 1])
        else:
            break

    # for i in range(R):
    #     for j in range(C):
    #         print(rcMap[i][j], end=' ')
    #
    #     print()
    # print()
    #
    #
    # for i in range(R):
    #     for j in range(C):
    #         print(dis[i][j], end=' ')
    #
    #     print()
    # print()



    while len(wque):
        if wque[0][2] == cur:
            x, y, t = wque.pop(0)

            if wChk[x][y]:
                continue
            else:
                wChk[x][y] = True

            for i in range(4):
                if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C and rcMap[x + dx[i]][y + dy[i]] != 'X' and rcMap[x + dx[i]][y + dy[i]] != 'D' and not wChk[x + dx[i]][y + dy[i]]:
                    # 가려는 곳이 돌, 비버 소굴 아니고 가본적 없을때
                    wque.append([x + dx[i], y + dy[i], t + 1])
                    rcMap[x + dx[i]][y + dy[i]] = '*'

        else:
            break
    cur += 1
    #
    # for i in range(R):
    #     for j in range(C):
    #         print(rcMap[i][j], end=' ')
    #
    #     print()
    # print()


if dis[D[0]][D[1]] == 0:
    print("KAKTUS")
else:
    print(dis[D[0]][D[1]])

