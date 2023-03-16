import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
rc = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0


for i in range(N - 1):
    for j in range(i + 1, N):
        if rc[i][0] + rc[j][0] <= H and rc[i][1] <= W and rc[j][1] <= W:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])

        if rc[i][0] + rc[j][0] <= W and rc[i][1] <= H and rc[j][1] <= H:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])

        if rc[i][0] + rc[j][1] <= H and rc[i][1] <= W and rc[j][0] <= W:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])

        if rc[i][0] + rc[j][1] <= W and rc[i][1] <= H and rc[j][0] <= H:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])




        if rc[i][1] + rc[j][0] <= H and rc[i][0] <= W and rc[j][1] <= W:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])

        if rc[i][1] + rc[j][0] <= W and rc[i][0] <= H and rc[j][1] <= H:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])

        if rc[i][1] + rc[j][1] <= H and rc[i][0] <= W and rc[j][0] <= W:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])

        if rc[i][1] + rc[j][1] <= W and rc[i][0] <= H and rc[j][0] <= H:
            ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0] * rc[j][1])


print(ans)