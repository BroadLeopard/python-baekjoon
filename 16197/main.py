import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 1000000000

def judge(x , y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False


def func(cnt, x1, y1, x2, y2):
    global ans

    if cnt > 10:
        ans = min(ans, 11)
    elif judge(x1, y1) and judge(x2, y2):#둘 다 내부
        x3, y3, x4, y4 = 0, 0, 0, 0
        for k in range(4):
            if judge(x1 + dx[k], y1 + dy[k]) and judge(x2 + dx[k], y2 + dy[k]):#다음에도 내부에 있는 경우
                if nMap[x1 + dx[k]][y1 + dy[k]] == '#':
                    x3 = x1
                    y3 = y1
                else:
                    x3 = x1 + dx[k]
                    y3 = y1 + dy[k]

                if nMap[x2 + dx[k]][y2 + dy[k]] == '#':
                    x4 = x2
                    y4 = y2
                else:
                    x4 = x2 + dx[k]
                    y4 = y2 + dy[k]

                func(cnt + 1, x3, y3, x4, y4)

            else:#둘 중 하나라도 떨어지는 경우
                func(cnt + 1, x1 + dx[k], y1 + dy[k], x2 + dx[k], y2 + dy[k])


    elif judge(x1, y1) or judge(x2, y2):#둘 중 하나만 내부
        ans = min(ans, cnt)


N, M = map(int, sys.stdin.readline().split())

nMap = []

coin = []

for i in range(N):
    nMap.append(list(sys.stdin.readline()[:-1]))
    for j in range(M):
        if nMap[i][j] == 'o':
            coin.extend([i, j])

func(0, coin[0], coin[1], coin[2], coin[3])
if ans == 11:
    print(-1)
else:
    print(ans)



