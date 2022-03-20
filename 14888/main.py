import sys

big = -1000000000
small = 1000000000


def func(left, li, num):
    if num == 0:
        global big, small
        su = A[0]
        for i in range(N - 1):
            if left[i] == 0:
                su += A[i+1]
            elif left[i] == 1:
                su -= A[i+1]
            elif left[i] == 2:
                su *= A[i+1]
            else:
                if su < 0:
                    su = -su
                    su //= A[i+1]
                    su = -su
                else:
                    su //= A[i+1]

        big = max(big, su)
        small = min(small, su)

    else:
        for i in range(4):
            if li[i] > 0:
                li[i] -= 1
                func(left + [i], li, num - 1)
                li[i] += 1


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

func([], op, N - 1)

print(big)
print(small)
