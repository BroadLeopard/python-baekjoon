import sys

N, M = map(int, sys.stdin.readline().split())
li = [[] for _ in range(N + 1)]
chk = [0 for _ in range(N + 1)]
start, end = 0, 0

ans = 0

for _ in range(N):
    A, B, C = map(int, sys.stdin.readline().split())
    li[A].append([B, C])
    li[B].append([A, C])

start, end = map(int, sys.stdin.readline().split())

que = []

for d, m in li[start]:
    que.append([d, m])

while que:
    s, v = que.pop(0)

    if chk[s] < v:
        chk[s] = v

        for d, m in li[s]:
            que.append([d, m])


print(chk[end])