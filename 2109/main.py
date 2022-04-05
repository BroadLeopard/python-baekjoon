import sys
import heapq
from collections import deque

N = int(sys.stdin.readline())
pd = []
ans = 0
maxDay = -1
hpq = []

for _ in range(N):
    pd.append(list(map(int, sys.stdin.readline().split())))  # p, d

if N == 0:
    print(0)
    exit(0)

pd.sort(key=lambda x: (-x[1], -x[0]))

deq = deque(pd)

maxDay = pd[0][1]

for curDay in range(maxDay, 0, -1):
    while deq and curDay == deq[0][1]:
        heapq.heappush(hpq, -deq[0][0])
        deq.popleft()

    if hpq:
        ans -= hpq[0]
        heapq.heappop(hpq)

print(ans)
