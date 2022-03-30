import sys

T = int(sys.stdin.readline())

net = [False, False] + [True]*9999

for i in range(2, 10000):
    if net[i]:
        tmp = 2 * i
        while tmp < 10000:
            net[tmp] = False
            tmp += i



for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    chk = [False for _ in range(10001)]
    dis = [100000 for _ in range(10001)]
    que = [a]
    chk[a] = True
    dis[a] = 0

    while que:
        tmp = que.pop(0)

        if tmp == b:
            break

        for i in range(4):  # 천, 백, 십, 일자릿수
            stmp = str(tmp)

            for j in range(10):
                stmp = stmp[:i] + str(j) + stmp[i + 1:]  # 해당 자릿수를 바꿈
                tmp2 = int(stmp)

                if 1000 < tmp2 < 10000 and net[tmp2] and not chk[tmp2] and dis[tmp2] > dis[tmp] + 1:  # 바꾼 수가 소수일 경우
                    dis[tmp2] = dis[tmp] + 1
                    que.append(tmp2)
                    chk[tmp2] = True  # 이 수는 더이상 큐에 안 넣는다.


    print(dis[b])
