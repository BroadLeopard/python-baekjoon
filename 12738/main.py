import sys


dx = [2, 1, 2, 1]
dy = [1, 2, -1, -2]

def func(x, y , cnt):
    if cnt < 5:
        global ans
        ans = max(cnt, ans)

        # print(x, y , cnt)

        for i in range(4):
            if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N:
                func(x + dx[i], y + dy[i], cnt + 1)


N, M = map(int, sys.stdin.readline().split())
n, m = 0, 0
ans = 1


if N >= 3 and M >= 7:
    ans = M - 2
else:
    func(0, 0, 1)
    ans = min(ans, 4)


print(ans)