import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
li = []

for _ in range(N):
    h, w = map(int, sys.stdin.readline().split())

    if H > W and h > w:
        li.append([h, w])




