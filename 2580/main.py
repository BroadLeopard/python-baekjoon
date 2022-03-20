import sys

sudoku = [0 for _ in range(9)]
lis = []

def xChk(x, i):
    if i in sudoku[x]:  # x축 확인
        return False
    return True

def yChk(y, i):
    for k in range(9):
        if sudoku[k][y] == i: #y축 확인
            return False

    return True

def boxChk(x, y, i):
    a = x // 3 * 3
    b = y // 3 * 3

    for tmpMap in sudoku[a: a + 3]:  # 박스 확인
        if i in tmpMap[b: b + 3]:
            return False

    return True


def func(lisLength):
    if lisLength == len(lis):
        for p in sudoku:
            print(*p)

        exit(0)

    else:
        x, y = lis[lisLength]
        for i in range(1, 10):# i를 넣어도 되는지 확인
            if xChk(x, i) and yChk(y, i) and boxChk(x, y, i):
                sudoku[x][y] = i
                func(lisLength + 1)
                sudoku[x][y] = 0


for i in range(9):
    sudoku[i] = list(map(int, sys.stdin.readline().split()))

    for j in range(9):
        if sudoku[i][j] == 0:
            lis.append([i, j])

func(0)
