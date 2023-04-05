import sys
# Press the green button in the gutter to run the script.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 64


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    def watch(myMap, dir, i, j):
        k = 1
        while 0 <= i + dx[dir] * k < N and 0 <= j + dy[dir] * k < M:
            if myMap[i + dx[dir] * k][j + dy[dir] * k] == 6:
                break
            elif myMap[i + dx[dir] * k][j + dy[dir] * k] == 0:
                myMap[i + dx[dir] * k][j + dy[dir] * k] = '#'
            k += 1

        return myMap


    def func(nm, l):
        if len(l) == 0:
            tmp = 0
            global answer
            for i in range(N):
                for j in range(M):
                    if nm[i][j] == 0:
                        tmp += 1

            for i in range(N):
                print(nm[i])

            print()

            answer = min(tmp, answer)
        else:
            x, y = l.pop()
            if nm[x][y] == 1:
                for i in [0, 1, 2, 3]:
                    tmp = [item[:] for item in nm]
                    tmp = watch(tmp, i, x, y)
                    func(tmp, l)

            elif nm[x][y] == 2:
                for i, j in [[0, 2], [1, 3]]:
                    tmp = [item[:] for item in nm]
                    tmp = watch(tmp, i, x, y)
                    tmp = watch(tmp, j, x, y)
                    func(tmp, l)

            elif nm[x][y] == 3:
                for i, j in [[0, 1], [1, 2], [2, 3], [3, 0]]:
                    tmp = [item[:] for item in nm]
                    tmp = watch(tmp, i, x, y)
                    tmp = watch(tmp, j, x, y)
                    func(tmp, l)

            elif nm[x][y] == 4:
                for i, j, k in [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]:
                    tmp = [item[:] for item in nm]
                    tmp = watch(tmp, i, x, y)
                    tmp = watch(tmp, j, x, y)
                    tmp = watch(tmp, k, x, y)
                    func(tmp, l)


    li = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] in [1,2,3,4,5]:
                if arr[i][j] == 5:
                    for t in range(4):
                        arr = watch(arr, t, i, j)
                else:
                    li.append([i, j])

    for i in range(N):
        print(arr[i])

    func(arr, li)

    print(answer)