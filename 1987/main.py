import sys

ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]




def func(li, x, y, cnt):
    global ans

    if li[ord(keyboard[x][y]) - 65]:
        ans = max(ans, cnt)
    else:
        for i in range(4):
            if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C and chk[x + dx[i]][y + dy[i]]:
                chk[x][y] = False
                li[ord(keyboard[x][y]) - 65] += 1
                func(li, x + dx[i], y + dy[i], cnt + 1)
                li[ord(keyboard[x][y]) - 65] -= 1
                chk[x][y] = True
            else:
                ans = max(ans, cnt)


R, C = map(int, sys.stdin.readline().split())

keyboard = []
chk = []

for _ in range(R):
    keyboard.append(list(sys.stdin.readline()[:-1]))
    chk.append([True] * C)

alpha = [0] * 26

func(alpha, 0, 0, 0)#여태까지 넣은 알파벳, 그리고 다음에 이동할 위치, 길이

print(ans)



