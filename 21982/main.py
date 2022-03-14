import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, x = map(int, sys.stdin.readline().split())# stdin에서 입력을 받는다.
    hs, ha, hb, hc = map(int, sys.stdin.readline().split())# stdin에서 입력을 받는다.
    ws, wa, wb, wc = map(int, sys.stdin.readline().split())# stdin에서 입력을 받는다.

    H, W, V = [0 for i in range(n)], [0 for i in range(n)], [0 for i in range(n)]

    H[0] = hs % hc + 1
    W[0] = ws % wc + 1
    for i in range(1, n):
        H[i] = H[i-1] + 1 + (H[i-1] * ha + hb) % hc
        W[i] = (W[i-1] * wa + wb) % wc + 1

    answer = -1


    print(answer)