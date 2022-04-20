import sys

N, M = map(int, sys.stdin.readline().split())
li = [[0 for _ in range(N + 1)] for _ in range(N+1)]
ans = 0


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    li[a][b] = 1
    li[b][a] = 1


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if i == j or j == k or k == i:#같은거는 ㄴㄴ
                continue
            
            if li[j][k] or li[i][k] or li[j][i]:
                continue

            ans += 1

print(ans // 6)

