import sys

answer = 0


def func(x, cnt):#이번 단계에서 찍을 퀸의 행, 현재 있는 퀸의 수
    if cnt == N:
        global answer
        answer += 1

        # for t in range(N):
        #     print(*nMap[t])

       # print()
    else:
        for k in range(N):
            flag = False

            for j in range(N):#같은 열에 있는지 확인
                if nMap[j][k] == 1:
                    flag = True
                    break

            if flag:
                continue

            for p in range(x + 1):
                if 0 <= k - p and nMap[x-p][k-p] == 1:#왼쪽 대각선 확인
                    flag = True
                    break

                if k + p < N and nMap[x-p][k+p] == 1:#오른쪽 대각선 확인
                    flag = True
                    break

            if flag:
                continue


            nMap[x][k] = 1
            func(x+1, cnt + 1)
            nMap[x][k] = 0


N = int(sys.stdin.readline())
nMap = [[0 for _ in range(N)] for _ in range(N)]

func(0, 0)

print(answer)


