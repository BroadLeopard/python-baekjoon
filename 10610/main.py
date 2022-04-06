import sys


N = list(sys.stdin.readline()[:-1])

N.sort(reverse=True)

if '0' != N[-1] or sum(list(map(int, N))) % 3 != 0:
    print(-1)
    exit(0)

print(''.join(N))


