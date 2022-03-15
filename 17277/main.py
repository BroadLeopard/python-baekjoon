import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, X, y, Z = map(int, sys.stdin.readline().split())
    V = list(map(int, sys.stdin.readline().split()))

    sum = 0
    flag = True


    for i in range(n - 1, -1, -1):
        if X < y:
            break
        else:
            X = X - y
            sum += V[i] - y

            if sum >= Z:
                print(i + 1, n)
                flag = False
                break


    if flag:
        print(-1)
