import sys

N, M = map(int, sys.stdin.readline().split())
li = [[] for _ in range(N + 1)]# 섬 번호와 다리 무게 제한
start, end = 0, 0
left, right = 0, 0
ans = 0

for _ in range(N):
    A, B, C = map(int, sys.stdin.readline().split())#연결 통로
    li[A].append([B, C])
    li[B].append([A, C])
    right = max(right, C)

start, end = map(int, sys.stdin.readline().split())#출발지, 도착지

while left <= right:
    mid = (left + right) // 2
    que = [start]

    chk = [False for _ in range(N + 1)]  # 현재 섬 방문 유무
    chk[start] = True


    while que:
        tmp = que.pop(0)

        for d, m in li[tmp]:
            if mid > m or chk[d]: # 방문한 적 있거나, 무게 견딜 수 없는 경우
                continue

            chk[d] = True

            que.append(d)

    if not chk[end]:#도달한적 없으니 무게를 낮춘다.
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)