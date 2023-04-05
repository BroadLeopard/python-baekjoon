import sys
from collections import deque

if __name__ == '__main__':
    N, M, T = map(int, sys.stdin.readline().split())
    circle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    xdk = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    answer = 0
    dx = [0, 1, 0]
    dy = [1, 0, -1]
    visit = [[0 for _ in range(M)] for _ in range(N)]


    def func(i, j):#bfs로
        val = circle[i][j]
        circle[i][j] = 0
        que = deque([[i, j]])
        cnt = 0

        # if i == 2 and j == 2:
        #     print()

        while que:
            x, y = que.popleft()

            if visit[x][y]:
                continue

            visit[x][y] = 1



            for k in range(3):
                if 0 <= x + dx[k] < N:
                    t = y + dy[k]

                    if t == -1:
                        t = M - 1
                    elif t == M:
                        t = 0

                    if val == circle[x + dx[k]][t] and visit[x + dx[k]][t] == 0:
                        cnt += 1
                        que.append([x + dx[k], t])
                        circle[x + dx[k]][t] = 0


        if cnt == 0:
            circle[i][j] = val

        return cnt


    for x, d, k in xdk:
        visit = [[0 for _ in range(M)] for _ in range(N)]

        for i, subCircle in enumerate(circle):

            deq = deque(subCircle)
            if (i + 1) % x == 0:
                if d: #d는 1인 경우
                    deq.rotate(-k)
                else: #d는 0인 경우
                    deq.rotate(k)

                circle[i] = list(deq)

        flag = 0
        # print('삭제전')
        # print(circle)

        for i in range(N):
            for j in range(M):
                if circle[i][j]: # 0 아니고
                    flag += func(i, j)#두 개라도 지웠으면 1 받는다

        # print('삭제후')
        # print(circle)
        #
        # print(flag, "flag")

        if flag == 0:
            cnt = 0
            tmpSum = 0

            for i in range(N):
                for j in range(M):
                    if circle[i][j]:
                        cnt += 1
                        tmpSum += circle[i][j]

            m = tmpSum / cnt

            for i in range(N):
                for j in range(M):
                    if circle[i][j]:
                        if circle[i][j] > m:
                            circle[i][j] -= 1
                        elif circle[i][j] < m:
                            circle[i][j] += 1


    for i in range(N):
        answer += sum(circle[i])

    print(answer)