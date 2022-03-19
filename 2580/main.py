import sys

sudoku = []
lis = []


def func():
    if not lis:
        for p in range(9):
            print(" ".join(list(map(str, sudoku[p]))))

        print()

        return 1

    else:
        x, y = lis.pop()
        for i in range(1, 10):# i를 넣어도 되는지 확인
            if i in sudoku[x]: #x축 확인
                continue

            flag = False

            for k in range(9):
                if sudoku[k][y] == i: #y축 확인
                    flag = True

            if flag:
                continue

            a = x // 3
            b = y // 3

            for tmpMap in sudoku[3 * a: 3 * a + 3]:# 박스 확인
                if i in tmpMap[3 * b: 3 * b + 3]:
                    flag = True
                    break

            if flag:
                continue

            sudoku[x][y] = i

            if func():
                return 1

        sudoku[x][y] = 0
        lis.append([x, y])
        return 0




for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
            lis.append([i, j])

answer = func()
