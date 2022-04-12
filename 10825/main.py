import sys

N = int(sys.stdin.readline())
li = []

for _ in range(N):
    tmp = sys.stdin.readline()[:-1].split()
    tmp = [tmp[0]] + list(map(int, tmp[1:4]))
    li.append(tmp)

li.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for t in li:
    print(t[0])