import sys

def func(sx, ex, sy, ey):
    if sx + 2 == ex:
        li[sx][sy + 2] = '*'
        li[sx + 1][sy + 1] = '*'
        li[sx + 1][sy + 3] = '*'
        for i in range(5):
            li[sx + 2][sy + i] = '*'
    else:
        func(sx, (sx + ex)//2, (3 * sy + ey) // 4 +1, (sy + 3 * ey)//4)
        func((sx+ex)//2 + 1, ex, sy, (sy + ey) // 2)
        func((sx+ex)//2 + 1, ex, (sy + ey) // 2 + 1, ey)


N = int(sys.stdin.readline())
li = [[' ' for _ in range(2 * N)] for _ in range(N)]


func(0, N - 1, 0, 2 * N - 1)

for i in range(N):
    for j in range(2*N):
        print(li[i][j], end='')

    print()

