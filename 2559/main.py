import sys

N, K = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

tmp = sum(t[:K])
ans = tmp

for i in range(N - K):
    tmp = tmp - t[i] + t[i + K]
    ans = max(ans, tmp)


print(ans)

