import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


num = 0

def func(i, j):
    global num
    num += 1
    reserved = [[i, j]]
    que = [[i, j]]
    chk[i][j] = True
    cnt = 0

    while que:
        x, y = que.pop(0)

        for t in range(4):
            if 0 <= x + dx[t] < N and 0 <= y + dy[t] < M and li[x + dx[t]][y + dy[t]] == "0" and not chk[x + dx[t]][y + dy[t]]:
                reserved.append([x + dx[t], y + dy[t]])
                que.append([x + dx[t], y + dy[t]])
                chk[x + dx[t]][y + dy[t]] = True

    cnt = len(reserved)

    for x, y in reserved:
        zeroMap[x][y] = [cnt, num]



N, M = map(int, sys.stdin.readline().split())
li = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
chk = [[False for _ in range(M)] for _ in range(N)]
zeroMap = [[0 for _ in range(M)] for _ in range(N)]
answer = [['0' for _ in range(M)] for _ in range(N)]


for i in range(N):
     for j in range(M):
         if li[i][j] == '0' and chk[i][j] == False:
             func(i, j)


#
# for i in range(N):
#      print(*zeroMap[i])


for i in range(N):
    for j in range(M):
        if li[i][j] == "1":
            tmp = 1
            tli = []

            for t in range(4):
                if 0 <= i + dx[t] < N and 0 <= j + dy[t] < M:
                    if li[i + dx[t]][j + dy[t]] == "0":
                        if zeroMap[i + dx[t]][j + dy[t]][1] not in tli:
                            tli.append(zeroMap[i + dx[t]][j + dy[t]][1])
                            tmp = (tmp + zeroMap[i + dx[t]][j + dy[t]][0]) % 10

            answer[i][j] = str(tmp)

for i in range(N):
    print("".join(answer[i]))



