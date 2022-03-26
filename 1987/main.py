import sys

ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
path = [False] * 26

def func(x, y, cnt):#여태까지 넣은 알파벳, 그리고 다음에 이동할 위치 x y, 현재까지 이동한 길이
    global ans

    path[ord(keyboard[x][y]) - 65] = True

    for i in range(4):
        if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C and not path[ord(keyboard[x + dx[i]][y + dy[i]]) - 65]:
            # 다음에 올 알파벳은 지나간 적이 없는 경우 이때 알파벳이 경로도 포함한다.
            func(x + dx[i], y + dy[i], cnt + 1)
        else:
            ans = max(ans, cnt)

    path[ord(keyboard[x][y]) - 65] = False



R, C = map(int, sys.stdin.readline().split())

keyboard = []

for _ in range(R):
    keyboard.append(list(sys.stdin.readline()[:-1]))


func(0, 0, 1)

print(ans)
