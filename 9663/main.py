import sys

N = 0

def func(x, y, xl, yl):
    if xl[x] or yl[y]:
        return 0
    else:
        xl[x] = True
        yl[y] = True

        if False not in xl and False not in yl:
            return 1
        else:
            hap = 0
            if x + 1 < N:
                hap += func(x+1, y, xl, yl)
            elif y + 1 < N:
                hap += func(x, y+1, xl, yl)
            return hap

N = int(sys.stdin.readline())
xl = [False] * N
yl = [False] * N

print(func(0, 0, xl, yl))
