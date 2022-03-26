import sys

N, M = map(int, sys.stdin.readline().split())

li = [0] * 111
que = [1]
dp = [0, 0] + [100000] * 110#넉넉하게 110까지 했습니다.


for _ in range(N + M):
    x, y = map(int, sys.stdin.readline().split())
    li[x] = y#사다리나 뱀을 탈 경우입니다 그 외에는 값을 0으로 했습니다


while len(que) != 0:
    tmp = que.pop(0)

    for i in range(1, 7):
        if i + tmp < 102:
            if li[i + tmp] != 0 and dp[li[i + tmp]] > dp[tmp] + 1:#사다리나 뱀을 탈 경우에, 목적지가 기존 값보다 크면 바꾸기 위함입니다.
                dp[li[i + tmp]] = dp[tmp] + 1
                dp[i + tmp] = dp[tmp] + 1
                que.append(li[i + tmp])

            if dp[i + tmp] > dp[tmp] + 1:
                dp[i + tmp] = dp[tmp] + 1
                que.append(i + tmp)

# for i in range(1, 108):
#     print(i, dp[i])
print(dp[100])


