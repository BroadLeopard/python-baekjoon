import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = list(map(int, sys.stdin.readline().split()))
    mMap = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        mMap[a][b] = 1
        mMap[b][a] = 1

    V = [0] * (N + 1)
    R = [1]

    answer = -1

    while sum(V) != N:
        tmp = R.pop()
        if V[tmp] == 0:#방문하지 않았다면
            V[tmp] = 1
            answer += 1
            for i in range(1, N +1):
                if mMap[tmp][i] == 1 and V[i] == 0 and i not in R:
                    R.append(i)

    print(answer)


