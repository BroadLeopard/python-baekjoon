import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
MV = []
C = []

i = 0
ans = 0

for _ in range(N):
    MV.append(list(map(int, sys.stdin.readline().split())))# 무게, 가치

for _ in range(K):
    C.append(int(sys.stdin.readline()))

MV.sort()
C.sort()

hpq = []

i = 0
l = len(MV)

for c in C:
    while i < l and MV[i][0] <= c:
        heapq.heappush(hpq, -MV[i][1])
        i += 1

    if hpq:
        ans -= hpq[0]
        heapq.heappop(hpq)

print(ans)
