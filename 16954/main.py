import sys


nMap = [[['.' for _ in range(8)] for _ in range(8)] for _ in range(9)]
chk = [[[False for _ in range(8)] for _ in range(8)] for _ in range(9)]


for i in range(8):
    nMap[0][i] = list(sys.stdin.readline()[:-1])

for i in range(1, 9):
    for j in range(1, 8):
        for k in range(8):
            if nMap[i-1][j-1][k] == '#':
                nMap[i][j][k] = '#'


que = [[0, 7, 0]]

dx = [0, 0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 0, -1, 1, 1, -1]


while len(que):
    t, x, y = que.pop(0)

    if x == 0 and y == 7:
        print(1)
        exit(0)

    if chk[t][x][y]:
        continue
    else:
        chk[t][x][y] = True

    for i in range(9):
        if t < 8:
            if 0 <= x + dx[i] < 8 and 0 <= y + dy[i] < 8 and nMap[t + 1][x + dx[i]][y + dy[i]] != '#' and nMap[t][x + dx[i]][y + dy[i]] != '#':
                que.append([t + 1, x + dx[i], y + dy[i]])
        else:
            print(1)
            exit(0)

print(0)
