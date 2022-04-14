import sys

def func(x):
    cnt = 0
    while x % 3 == 0:
        cnt += 1
        x //= 3
    return cnt


N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li2 = []

for tmp in li:
    li2.append([func(tmp), tmp])


li2.sort(key=lambda x: (-x[0], x[1]))

for tmp in li2:
    print(tmp[1], end=' ')

