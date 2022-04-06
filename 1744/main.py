import sys
from collections import deque


N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0

li.sort()
deq = deque(li)

while len(deq) > 1 and deq[0] < 0 and deq[1] < 0:  # 둘 다 음수인 경우
    ans += deq[0] * deq[1] if deq[0] * deq[1] > deq[0] + deq[1] else deq[0] + deq[1]
    deq.popleft()
    deq.popleft()


while len(deq) > 1 and deq[-2] > 0 and deq[-1] > 0:# 둘 다 양수
    ans += deq[-2]*deq[-1] if deq[-2] * deq[-1] > deq[-2] + deq[-1] else deq[-2] + deq[-1]
    deq.pop()
    deq.pop()

#현재 음수 0 ~ 1개 0 0~여러개 양수 0 ~ 1개 남아있는 상황

while len(deq) > 1:
    ans += deq[0] * deq[1] if deq[0] * deq[1] > deq[0] + deq[1] else deq[0] + deq[1]
    deq.popleft()
    deq.popleft()


if deq:
    ans += deq[0]

print(ans)