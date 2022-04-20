import sys

def func(pre, x, y, l):
    if l == 6:
        s.add(pre)
    else:
        for i in range(4):
            if 0 <= x + dx[i] < 5 and 0 <= y + dy[i] < 5:
                func(pre + li[x + dx[i]][y + dy[i]], x + dx[i], y + dy[i], l + 1)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

li = [sys.stdin.readline().split() for i in range(5)]
s = set()

for i in range(5):
    for j in range(5):
        func('', i, j, 0)

print(len(s))
