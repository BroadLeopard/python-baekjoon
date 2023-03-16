import sys

N, M = map(int, sys.stdin.readline().split())
li = []
chk = []
ans = 0
ansLi = []

for _ in range(N):
    tmp = sys.stdin.readline()[:-1]
    li.append(tmp)
    chk.append(list(tmp))


for i in range(N):
    for j in range(M):
        flag = False
        if li[i][j] == '*':#한 점이 *
            l = 0
            for k in range(1, 100):
                if i + k < N and k <= i and j + k < M and k <= j:
                    if li[i + k][j] == '*' and li[i - k][j] == '*' and li[i][j + k] == '*' and li[i][j - k] == '*':
                        l = k
                    else:
                        break

                else:
                    break


            if l > 0:
                ansLi.append([i+1, j + 1, l])
                chk[i][j] = '.'
                for k in range(1, l + 1):
                    chk[i + k][j] = '.'
                    chk[i - k][j] = '.'
                    chk[i][j + k] = '.'
                    chk[i][j - k] = '.'

for i in range(N):
    for j in range(M):
        if chk[i][j] == '*':
            print(-1)
            exit(0)


print(len(ansLi))
for tmpLi in ansLi:
    print(*tmpLi)

