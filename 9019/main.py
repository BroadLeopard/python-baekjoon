import sys
from collections import deque

N = int(sys.stdin.readline())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())

    que = [[A, '']]
    res = [True for i in range(10010)]

    while True:
        tmp, ans = que.pop(0)

        r1 = tmp * 2 % 10000

        if res[r1]:
            res[r1] = False
            que.append([r1, ans + 'D'])

            if r1 == B:
                break


        r2 = (tmp + 9999) % 10000

        if res[r2]:
            res[r2] = False
            que.append([r2, ans + 'S'])

            if r2 == B:
                break

        l = len(str(tmp))

        tmp = ['0' for i in range(4 - l)] + list(str(tmp))

        r3 = int(tmp[1] + tmp[2] + tmp[3] + tmp[0])

        if res[r3]:
            res[r3] = False
            que.append([r3, ans + 'L'])

            if r3 == B:
                break


        r4 = int(tmp[3] + tmp[0] + tmp[1] + tmp[2])

        if res[r4]:
            res[r4] = False
            que.append([r4, ans + 'R'])

            if r4 == B:
                break


    print(que[-1][1])

