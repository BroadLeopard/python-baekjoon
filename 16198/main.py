import sys

ans = -10000000000


def func(li, energy):
    l = len(li)

    if l == 2:
        global ans
        ans = max(ans, energy)
    else:
        for w in range(1, l - 1):
            func(li[:w] + li[w+1:], energy + li[w-1]*li[w+1])


N = int(sys.stdin.readline())
W = list(map(int, sys.stdin.readline().split()))

func(W, 0)

print(ans)





