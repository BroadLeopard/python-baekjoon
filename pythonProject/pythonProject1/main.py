import sys

N = int(sys.stdin.readline())
arr = []
x = 0
y = 0

size = 2
cnt = 0
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def func(x, y):
    visit = [[False for _ in range(N)] for _ in range(N)]

    que = [[x, y]]
    funcTime = 0

    while que:
        # print(que)
        #
        # for i in range(N):
        #     print(visit[i])
        # print(funcTime)
        # print()

        tmp = []
        candidate = []

        for tx, ty in que:
            if visit[tx][ty]:
                continue

            visit[tx][ty] = True

            for i in range(4):
                if 0 <= tx + dx[i] < N and 0 <= ty + dy[i] < N and visit[tx + dx[i]][ty + dy[i]] == False:
                    if 0 < arr[tx + dx[i]][ty + dy[i]] < size:
                        candidate.append([tx + dx[i], ty + dy[i]])
                    elif arr[tx + dx[i]][ty + dy[i]] <= size:
                        tmp.append([tx + dx[i], ty + dy[i]])


        if candidate:
            candidate.sort()
            rx, ry = candidate[0]
            arr[rx][ry] = 0
            return funcTime + 1, rx, ry

        funcTime += 1
        que = tmp

    return 0, 0, 0 #어른 상어 부를 시간



for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)

    if 9 in tmp:
        x = i
        y = tmp.index(9)
        arr[x][y] = 0

while True:
    # print('size', size)
    time, x, y = func(x, y)
    # print('time', time)
    #
    # for i in range(N):
    #     print(arr[i])
    # print('x', x, 'y', y)

    if time == 0:
        break
    else:
        cnt += 1

        if size == cnt:
            size += 1
            cnt = 0
            # print('size up, size is' , size)
        answer += time



    # print()



print(answer)