import sys

N, M = map(int, sys.stdin.readline().split())

li = [0] * 111
que = [1]
cnt = [0] * 111


for _ in range(N + M):
    x, y = map(int, sys.stdin.readline().split())
    li[x] = y#사다리나 뱀을 탈 경우입니다 그 외에는 값을 0으로 했습니다


while len(que) != 0:
    tmp = que.pop(0)

    for i in range(1, 7):
        if i + tmp < 101:
            y = i + tmp

            if li[y]:
                y = li[y]

            if cnt[y] == 0:
                cnt[y] = cnt[tmp] + 1
                que.append(y)

    # print(que)

print(cnt[100])

