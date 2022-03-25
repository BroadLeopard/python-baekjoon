import sys

ans = 0

N = int(sys.stdin.readline())
T = [0]
P = [0]
dp = [0] * 20

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(1, N + 1):
    dp[i + T[i] - 1] = max(dp[i + T[i] - 1], max(dp[:i]) + P[i])

print(max(dp[:N+1]))